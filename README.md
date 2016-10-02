# Sentence-Splitter-for-Russian
#### Sentence Boundary Detection in raw text input.


## Program
This program uses the pretrained model for Sentence Boundary Detection to process raw textual input and return it in sentence-by-sentence form with a single newline character separating different sentences in a file. Only dots, question marks, and exclamation marks are considered as potential sentence boundaries in this implementation.

## Model
The modelling approach used in this program was evaluated at 98% accuracy using 10-fold cross-validation on the training set. The final version of the model achieved 96% test accuracy on the Opencorpora.ru Corpus used as the test set. The program for training the model is presented in the Model-Training folder. 

For classification the model uses character-level embeddings of 14 characters: 7 directly preceding and 7 directly following characters near a potential sentence boundary, including special characters **and spaces**.

## Character-level Embeddings

Char embeddings used here are 64-dimesion vectors which were trained with the standard word2vec algorithm. Character dictionary consists of 150 most common characters for Russian, which cower full Russian alphabet (uppercase and lowercase), full English alphabet (uppercase and lowercase), and most commonly used punctuation symbols. There is a pretrained wildcard for unknow characters.

## License

Apache 2

## Authors

#### Alexandr Kotlyarov




