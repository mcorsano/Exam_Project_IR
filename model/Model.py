
class Model :

    
    def __init__(self) -> None:
        self._documents = {}
        self._terms = {}
        self._trigrams = {}


    def set_documents(self, documents) :
        self._documents = documents
    

    def set_terms(self, terms) :
        self._terms = terms


    def set_trigrams(self, trigrams) :
        self._trigrams = trigrams


    def get_documents(self) :
        return self._documents

    
    def get_terms(self) :
        return self._terms


    def get_trigrams(self) :
        return self._trigrams


    def get_document(self, id) :
        return self._documents.get(id)