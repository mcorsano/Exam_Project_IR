
from gensim.parsing.preprocessing import STOPWORDS

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

    def remove_stopwords(self) :
        for word in self._terms :
            if word.get_term() in STOPWORDS :
                self._terms.remove(word)
                
    def normalize(self) :
        for term in self._terms :
            term.to_lower()   
    
    def stem(self) :
        for term in self._terms :
            term.to_stem()

    def lemmatize(self) :
        for term in self._terms :
            term.to_lemma()