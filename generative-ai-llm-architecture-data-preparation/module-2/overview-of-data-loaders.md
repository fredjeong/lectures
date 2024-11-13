# Overview of Data Loaders

Using a data loaders enable us to handle and prepare data while training modells. 

- Efficient loading and preprocessing of textual data
- Memory optimisation
- Simplified data augmentation
- Handling multiple samples as a batch at a time


## Transformation on input text data
- Tokenising: `get_tokenizer('basic_english')`
- Numericalising (indexing): `build_vocab_from_iterator(map(tokenizer, sentences))`
- Resizing (padding): `torch.nn.utils.rnn.pad_sequence`
- Tensor conversion
