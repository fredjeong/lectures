# Tokenisation process

- Tokenisation is the process of breaking a sentence into smaller pieces.
- We use a tokeniser to generate tokens. 
- Tokenisation methods include word-based, character-based, and subword-based.

## Word-based tokenisation
- Text is divided into individual words.
- Pros: It preserves the semantic meaning of the text.
- Cons: Increases model's overall vocabulary.

## Character-based tokenisation
- Splits text into individual characters.
- Pros: Smaller vocabularies.
- Cons: May not convey the same information as entire words and increases input dimensionality and computational needs.

## Subword-based tokenisation
- Frequently used words unsplit and infrequent words are broken down
- Algorithms include:
    - WordPiece
    - Unigram
    - SentencePiece

