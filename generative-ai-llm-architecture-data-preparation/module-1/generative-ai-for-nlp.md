# Generative AI for NLP

## Evolution of NLP
1. Rule-based system
    - Simply follows predefined linguistic rules
    - Accurate but lacking flexibility
2. Machine-learning based approach
    - Learn from various datasets and make predictions
    - More adaptive but limited understanding in complex language nuances
3. Deep learning architecture
4. Transformer
    - Designed specifically to handle sequential data
    - Understand context and dependencies within language

## Language Models

### GPT
- Acts as a decoder
- Adept at generating text
- Used in chatbots

### BERT (Bidrectional Encoder Representation Transformers)
- Utilises encoder-only transformer architecture
- Understands the context of a word in a sequence
- Used in sentiment analysis and question-answering

### BART (Bidirectional Autoregressive Transformers)
- Uses encoder-decoder architecture
- Versatile for various NLP tasks

### T5 (Text to Text Transfer Transformer)
- Uses encoder-decoder architecture
- Versatile for various NLP tasks

## GPT vs ChatGPT
- GPT focuses on diverse text generation tasks, whereas ChatGPT focuses on generating conversations.
- Training and fine-tuning of GPT is supervised-learning, whereas ChatGPT also utilises reinforcement learning (RLHF) for fine tuning.

## Versatility of LLMs
- Pre-train for generic purposes
- Fine-tune for a smaller dataset
- 예를 들면, 텍스트 분류라는 넓은 범위의 작업에 특화된 모델을 사전훈련시키고, retail industry에 맞게 fine-tuning을 거치면 된다.
