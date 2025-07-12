# --------------- requirements -----------------
# pip install openai pandas tqdm

import pandas as pd, openai, itertools, os, json
from pathlib import Path
from tqdm import tqdm

# ---------- config ----------
CSV_IN  = "citations_exactdup.csv"
CSV_OUT = "citations_with_all_duplicates.csv"
MODEL   = "gpt-3.5-turbo"          # or "gpt-4o-mini" etc.
THRESH  = 0.9                      # only ask GPT if difflib ratio < THRESH
openai.api_key = os.getenv("OPENAI_API_KEY")   # or paste your key

# ---------- helper ----------
def ask_llm_same_paper(title1, title2):
    """Return True iff GPT judges two titles are for the same paper."""
    msg = ( "You are a factual assistant. "
            "Reply with ONLY 'YES' or 'NO'.\n\n"
            f"Title 1: {title1}\nTitle 2: {title2}\n\n"
            "Are these titles about the same scientific paper?" )
    rs = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": msg}],
            temperature=0)
    return rs.choices[0].message.content.strip().upper() == "YES"

# ---------- main ----------
df = pd.read_csv(CSV_IN)
title_col = next(c for c in df.columns if c.lower().strip()=="title")
titles = df[title_col].astype(str).fillna("").tolist()
n = len(titles)

# exact-match flag already present; ensure column exists
if "exact_duplicate" not in df.columns:
    norm = [t.strip().lower() for t in titles]
    df["exact_duplicate"] = pd.Series(norm).duplicated(keep=False)

# prepare containers
df["llm_duplicate"] = False
df["duplicate_with"] = [[] for _ in range(n)]  # list of row indices

norm_titles = [t.strip().lower() for t in titles]
checked = {}   # (i,j) → True/False to avoid repeated LLM calls

# ---- loop over every unordered pair (i<j) ----
for i, j in tqdm(itertools.combinations(range(n), 2),
                 total=n*(n-1)//2, desc="Comparing"):
    # exact dup?  (already flagged)
    if norm_titles[i] == norm_titles[j]:
        df.at[i, "duplicate_with"].append(j)
        df.at[j, "duplicate_with"].append(i)
        continue

    # quick fuzzy filter to cut LLM cost (optional)
    import difflib
    if difflib.SequenceMatcher(None, norm_titles[i], norm_titles[j]).ratio() >= THRESH:
        pass  # run LLM
    else:
        continue  # clearly different

    # ask GPT once per unique pair
    key = (norm_titles[i], norm_titles[j])
    if key not in checked:
        checked[key] = ask_llm_same_paper(titles[i], titles[j])

    if checked[key]:
        df.at[i, "llm_duplicate"] = True
        df.at[j, "llm_duplicate"] = True
        df.at[i, "duplicate_with"].append(j)
        df.at[j, "duplicate_with"].append(i)

# convert duplicate_with lists to comma-separated strings for CSV
df["duplicate_with"] = (
    df["duplicate_with"]
      .apply(lambda lst: ",".join(map(str, sorted(set(lst)))) if lst else "")
)

df.to_csv(CSV_OUT, index=False)
print(f"✅ Saved → {CSV_OUT}")
