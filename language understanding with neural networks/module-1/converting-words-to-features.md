# Converting Words to Features

- One-hot encoding 
- bag of words
- embeddings
- embedding bags


## One-hot encoding
We convert words to numerical features so that machine learning models can process the text.
One-hot encoding is a method used to convert categorical data into feature vectors that a neural network can understand.
By doing so, we can represent each token as a vector (one-hot encoding vector)

The back of words representation portrays a document as the aggregate or average of one-hot encoded vectors. For example, for a sentence "I like cats", the bag of words vector is simply the sum of vectors for "I", "like", and "cats". 

## Embedding

Or we can simply use token indices instead of one-hot encoded vectors. The embedding layer accepts the index and outputs the embedding vector. The embedding weights are combined to form an embedding matrix (corresponding to the whole sentence).
The number of columns is the embedding dimension. Normally, embedding vectors have lower dimensionality compared to one-hot encoded vectors.