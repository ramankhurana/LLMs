# LLMs
Basic information(*) about LLMs available as open and closed source. 

| Model Series | Model Version | Number of Parameters | Open Source & License Terms | Features | Date of Release | Context Length | Pricing |
|--------------|---------------|----------------------|-----------------------------|----------|-----------------|----------------|---------|
| **LLaMA**    | LLaMA 2       | 7B, 13B, 70B         | Custom License (research and commercial use with restrictions) | General-purpose language understanding and generation |  July 2023        | 4,096 tokens   | Free for approved users |
| **LLaMA**    | LLaMA 3.1     | 8B, 70B, 405B        | Custom License (research and commercial use with restrictions) | Advanced language tasks, coding, multilingual support |  April 2024       | Up to 128,000 tokens | Free for approved users |
| **Mistral**  | Mistral 7B    | 7.3B                 | Apache 2.0                  | General-purpose language tasks; outperforms larger models on various benchmarks |  July 2024        | 128,000 tokens | Free |
| **Mistral**  | Mixtral 8x7B  | Mixture of Experts (MoE) model with 7B active parameters per expert | Apache 2.0 | Efficient handling of diverse tasks through MoE architecture |  July 2024        | 128,000 tokens | Free |
| **Mistral**  | Mistral Large 2 | 123B               | Apache 2.0                  | High-performance model for complex language tasks |  July 2024        | 128,000 tokens | Free |
| **Falcon**   | Falcon 7B     | 7B                   | Apache 2.0                  | Language understanding and generation; trained on web data |  May 2023         | 2,048 tokens   | Free |
| **Falcon**   | Falcon 40B    | 40B                  | Apache 2.0                   | Enhanced performance for various NLP tasks |  May 2023         | 2,048 tokens   | Free |
| **Falcon**   | Falcon 180B   | 180B                 | Apache 2.0                  | Competitive with state-of-the-art models in language tasks |  December 2023    | 2,048 tokens   | Free |
| **GPT-NeoX** | GPT-NeoX-20B  | 20B                  | Apache 2.0                  |  Autoregressive language generation for various NLP tasks |  April 2022       | 2,048 tokens   | Free |
| **MPT**      | MPT-7B        | 7B                   | Apache 2.0                  |  Commercially usable language model with extended context lengths |  May 2023         | 8,192 tokens   | Free |
| **MPT**      | MPT-30B       | 30B                  | Apache 2.0                  | Enhanced performance with longer context handling | June 2023        | 8,192 tokens   | Free |
| **RedPajama**| RedPajama-INCITE-7B | 7B            | Apache 2.0                   | Instruction-tuned and chat models for diverse NLP tasks |  July 2023        | 2,048 tokens   | Free |
| **StarCoder**| StarCoderBase | 15.5B                | OpenRAIL-M                  | Code-focused language model for programming tasks | May 2023         | 8,192 tokens   | Free |
| **Molmo**    | Molmo-70B     | 70B                  | Apache 2.0                  |  Multimodal capabilities; interprets images and interacts through chat | August 2024      | 4,096 tokens   | Free |
| **Molmo**    | Molmo-1B      | 1B                   | Apache 2.0                  |  Optimized for mobile devices; supports multimodal interactions |  August 2024      | 4,096 tokens   | Free |
| **GPT**      | GPT-1         | 117 million          | MIT License                |   Introduced the concept of generative pre-training for transformers. |  June 2018        | Not specified  | Free    |
| **GPT**      | GPT-2         | 1.5 billion          | MIT License                 |  Advanced language generation; capable of producing coherent and contextually relevant text. |  February 2019    | Not specified  | Free    |
| **GPT**      | GPT-3         | 175 billion          | Proprietary                |   Enhanced language understanding and generation; supports a wide range of NLP tasks. | June 2020        | 2,048 tokens   | Subscription-based |
| **GPT**      | GPT-3.5       | 175 billion          | Proprietary                 |  Improved performance over GPT-3; optimized for chat-based interactions. | 2022             | 4,096 tokens   | Subscription-based |
| **GPT**      | GPT-4         | Not publicly disclosed | Proprietary               |  Multimodal capabilities; processes text and images; improved reasoning abilities. |  March 2023       | 8,192 tokens   | Subscription-based |
| **GPT**      | GPT-4o        | Not publicly disclosed | Proprietary              |   Multimodal flagship model; enhanced accuracy; superior performance in non-English languages and vision tasks. | August 2024      | 128,000 tokens | Input: $2.50 per million tokens; Output: $10 per million tokens |
| **GPT**      | GPT-4o Mini   | Not publicly disclosed | Proprietary               |  Cost-effective model for simpler tasks; maintains multimodal capabilities. | August 2024      | 128,000 tokens | Subscription-based |
| **GPT**      | o1-preview    | Not publicly disclosed | Proprietary               |  Designed for complex reasoning; excels in science, coding, and math tasks. |   September 2024   | 128,000 tokens | Subscription-based |
| **GPT**      | o1-mini       | Not publicly disclosed | Proprietary               |  Lighter version of o1-preview; balances performance and efficiency. |  September 2024   | 128,000 tokens | Subscription-based |
| **Gemini**   | Gemini 1.0 Nano | Not publicly disclosed | Proprietary             |   Optimized for mobile devices; efficient performance |  November 2023    | Not publicly disclosed | Subscription-based |
| **Gemini**   | Gemini 1.5 Pro | Not publicly disclosed | Proprietary              |  Enhanced performance for complex tasks |February 2024    | Not publicly disclosed | Subscription-based |
| **Gemini**   | Gemini 1.0 Ultra | 1.5 trillion      | Proprietary                | High-end model with extensive capabilities |  November 2023    | Not publicly disclosed | Subscription-based |
| **Claude**   | Claude 1        | Not publicly disclosed | Proprietary             |      Initial version; proficient in various tasks with limitations in coding, math, and reasoning. | March 2023      | 9,000 tokens   | Subscription-based     |
| **Claude**   | Claude 2        | Not publicly disclosed | Proprietary             |      Expanded context window; ability to upload and process documents.  | July 2023       | 100,000 tokens | Subscription-based     |
| **Claude**   | Claude 2.1      | Not publicly disclosed | Proprietary             |      Doubled context window; improved accuracy and reduced false statements. | November 2023   | 200,000 tokens | Subscription-based     |
| **Claude**   | Claude 3 Haiku  | Not publicly disclosed | Proprietary              |    Fastest model; designed for high-speed AI interactions.| March 2024  | 200,000 tokens | $0.25 per million input tokens; $1.25 per million output tokens |
| **Claude**   | Claude 3 Sonnet | Not publicly disclosed | Proprietary              |     Balanced performance and speed; suitable for efficient, high-throughput tasks.       | March 2024      | 200,000 tokens | $3 per million input tokens; $15 per million output tokens |
| **Claude**   | Claude 3 Opus   | Not publicly disclosed | Proprietary               |    Most intelligent model; handles complex analysis and higher-order tasks.        | March 2024      | 200,000 tokens (expandable to 1 million for specific use cases) | $15 per million input tokens; $75 per million output tokens |
| **Claude**   | Claude 3.5 Sonnet | Not publicly disclosed | Proprietary             |    Improved performance in coding, workflows, and text extraction from images; introduces 'Artifacts' feature. |         | June 2024       | 200,000 tokens | Subscription-based     |
| **Claude**   | Claude 3.5 Haiku | Not publicly disclosed | Proprietary              |    Enhanced speed; suitable for lightweight tasks; includes 'computer use' capability.      | October 2024    | 200,000 tokens | Subscription-based     |
| **Nova**     | Nova Pro      | Not publicly disclosed | Proprietary               |   Tailored for various applications; scalable performance |   December 2023    | Not publicly disclosed | Subscription-based |
| **Phi**      | Phi-3         | Not publicly disclosed | Proprietary               |   Advanced reasoning and language capabilities |      March 2024       | Not publicly disclosed | Subscription-based |
| **Qwen**     | Qwen 2.5      | 0.5B to 72B          | Proprietary                |   Models ranging in size for diverse applications |   April 2024       | Not publicly disclosed | Subscription-based |
| **Nemotron** | Nemotron-4 340B | 340B               | Proprietary                |   High-parameter model for complex tasks |      May 2024         | Not publicly disclosed | Subscription-based |
| **Grok**     | Grok 2        | Not publicly disclosed | Proprietary             |      Enhanced capabilities for various applications |   June 2024        | Not publicly disclosed | Subscription-based |
| **Fugaku-LLM** | Fugaku-LLM-13B | 13B               | Proprietary               |    Japanese language model for diverse tasks |     July 2024        | Not publicly disclosed | Subscription-based |
| **DeepSeek** | DeepSeek-V3   | Not publicly disclosed | Proprietary              |     Advanced LLM with enhanced capabilities |       August 2024      | Not publicly disclosed | Subscription-based |
| **Orca**     | Orca          | Not publicly disclosed | Proprietary              |     Progressive learning model with complex reasoning |  September 2024   | Not publicly disclosed | Subscription-based |
 

(*)(Information to be double checked and verified)

