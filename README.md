# Sentence-Splitter-for-Russian
#### Sentence Boundary Detection in raw text input.

## How to use
Example:
```python
import Ru_splitter

testfile = open("testtext.txt", 'r')
input_text = testfile.read()
testfile.close()

splitter = Ru_splitter.Splitter()
sentence_list = splitter.split(input_text)

for i in sentence_list:
    print i
```

## How it works
This module uses the pretrained model for Sentence Boundary Detection to process raw textual input and return it in sentence-by-sentence form with a single newline character separating different sentences in a file. Only dots, question marks, and exclamation marks are considered as potential sentence boundaries in this implementation.

Preprocessing of the module collapses all whitesace and endline sequences into single space symbol if there are no endline symbols in the mix, a single newline symbol is used overwise. Single newline symbols are not removed and are treated as true sentence boundaries. They are treated as dots for the purpose of classification and later used to create sentence-by-sentence representation of the text which the module returns as a list.

## Model
The modelling approach used in this program was evaluated at 98% accuracy using 10-fold cross-validation on the training set. The final version of the model achieved 96% test accuracy on the Opencorpora.ru Corpus used as the test set. The program for training the model is presented in the Model-Training folder. 

For classification the model uses character-level embeddings of 14 characters: 7 directly preceding and 7 directly following characters near a potential sentence boundary, including special characters **and spaces**.

## Character-level Embeddings

Char embeddings used here are 64-dimesion vectors which were trained with the standard word2vec algorithm. Character dictionary consists of 150 most common characters for Russian, which cower full Russian alphabet (uppercase and lowercase), full English alphabet (uppercase and lowercase), and most commonly used punctuation symbols. There is a pretrained wildcard for unknow characters.


## Examples

Below are examples of correctly detected sentence boundaries. You can produce them yourself by running the program with the provided testtext.txt file.

```
«Обрыв»: журнал «Вестник Европы», 1869 г., № 1-5.
Первое отдельное издание — 1870 г.
-----------------------------------------
2 июля 2012 г. Банк России выпустил в обращение посвященную 200-летию со дня рождения писателя памятную монету номиналом 2 рубля с изображением И. А. Гончарова в серии «Выдающиеся личности России» .
Монета изготовлена из серебра 925-й пробы тиражом 5000 экземпляров и весом 17 граммов.
-----------------------------------------
Памятная монета Банка России, посвящённая 200-летию со дня рождения И. А. Гончарова.
2 рубля, серебро, 2012 год.
-----------------------------------------
Когда-то учился в технаре и был у нас учебник по спецухе.
Авторы муж и жена.
На обложке так были написаны: авторы - А.Я.Клешня, И.Я.Клешня.
-----------------------------------------
В помощь губернаторам созданы казённые и судебные палаты, другие гос. и соц. учреждения.
Губернаторы были подведомственны сенату.
-----------------------------------------
По всеобщей переписи 1897 года население составляло 129,2 млн человек.
Распределение населения по территориям было следующим: Европейская Россия — 94 244,1 тыс. чел., Польша — 9456,1 тыс. чел., Кавказ — 9354,8 тыс. чел., Сибирь — 5784,5 тыс. чел., Средняя Азия — 7747,1 тыс. чел., Финляндия — 2555,5 тыс. человек[13].
```

## License

Apache 2

## Authors

#### Alexandr Kotlyarov




