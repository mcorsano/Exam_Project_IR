# Exam Project IR

## Author 
Marianna Corsano

Introduction
=============
This is the project for the Information Retrieval Exam.  
It consists in a information retrieval systems able to answer boolean queries, phrase queries and wildcard queries providing also spelling correction of the query to be performed.

Corpus
======
The corpus consists of 42,306 documents.??? It is ..... movies extracted from the November 2, 2012 dump of English-language Wikipedia.  
Each document contains the Wikipedia movie ID followed by the title and the summary of the movie itself.  
The whole corpus is stored in a csv file.

Launch
======
The project comes with a simple graphic interface.  
To run the project:
```
python main.py
```

Technical details
=================

### How to perform the queries
The syntax allowed for the queries is the following:
* **boolean queries**: any number of words is allowed, separated by one among the operators AND, NOT, OR, specified in capital letters
* **phrase queries**: any number of word to be searched subsequently in the corpus is allowed
* **wildcard queries**: the wildcard operator used is the asterisk one (\*). While searching for a word, any number of wildcard operators is allowed.  

### Implementation details
The whole corpus is read only once when the program starts, ...

### Required external packages
* **nltk** - for lemmatization
```
pip install nltk
```
and then, from python console
```
import nltk
nltk.download('wordnet')
```
* **gensim** - for the stopwords
```
pip install gensim
```
* **re** - for the regular expressions
```
pip install regex
```
* **PySimpleGUI** - for the graphic interface
```
pip install PySimpleGUI
```
