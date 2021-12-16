
import csv
from model.Term import Term
from model.Document import Document 
from algorithm.Wildcard import Wildcard


class CsvReader :


    def __init__(self, filename) -> None :
        self._filename = filename
        self._documents = {}
        self._terms = {}
        self._trigrams = {}


    def read(self) :
        with open(self._filename, 'r', encoding="utf8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter = ';')
            for row in csv_reader :
                self._read_document(row)


    def _read_document(self, row) :
        id = row[0]
        title = row[1]
        summary = row[2]

        document = Document(id, title, summary)
        self._documents[document.get_id()] = document
        document.tokenize()
        document.remove_stopwords() 
        document.normalize()
        document.lemmatize()

        index = 0 
        for word in document.get_summary() :
            self._read_word(document, word, index)
            index += 1  

    
    def  _read_word(self, document, word, index) :
        if word in self._terms.keys() :
            term = self._terms.get(word)
            if term in document.get_terms().keys() :
                document.add_term(term, index)
            else :
                document.add_new_term(term, index)
                term.add_doc(document)
        else :
            term = Term(word)
            self._terms[word] = term
            document.add_new_term(term,index)

            term.add_doc(document)
        
        self._read_trigrams(word)
    

    def _read_trigrams(self, word) :
        trigrams = Wildcard().get_trigrams(word)
        for tri in trigrams :
            if tri in self._trigrams.keys() :
                self._trigrams[tri].append(word) 
            else :
                self._trigrams[tri] = [word]


    def get_all_documents(self) :
        return self._documents


    def get_all_terms(self) :
        return self._terms 

    
    def get_all_trigrams(self) :
        return self._trigrams
