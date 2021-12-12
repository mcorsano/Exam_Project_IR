
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from gensim.parsing.preprocessing import STOPWORDS
import re


class Document :


    def __init__(self, id, title, author, summary) -> None :
        self._id = int(id)
        self._title = title
        self._author = author
        self._summary = summary
        self._terms = []


    def __str__(self) :
        return str(self._id)


    def __repr__(self) :
        return str(self._id)


    def get_id(self) :
        return self._id


    def get_title(self) :
        return self._title


    def get_author(self) :
        return self._author


    def get_summary(self) :
        return self._summary


    def add_term(self, term) :
        self._terms.append(term)


    def get_terms(self) :
        return self._terms


    def tokenize(self) :
        self._summary = re.sub(r'[^\w\s]','', self._summary)
        self._summary = self._summary.split()


    def remove_stopwords(self) :
        self._summary = [word for word in self._summary if not word in STOPWORDS]


    def normalize(self) :
        self._summary = [word.lower() for word in self._summary]


    def lemmatize(self) :
        self._summary = [lemmatizer.lemmatize(word) for word in self._summary]





