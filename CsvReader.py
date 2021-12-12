
import csv
from Term import *
from Document import *
from gensim.parsing.preprocessing import STOPWORDS


class CsvReader :


    def __init__(self, filename) -> None :
        self._filename = filename
        self._documents = []
        self._terms = {}


    def read(self) :
        with open(self._filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter = ';')
            for row in csv_reader :
                id = row[0]
                title = row[1]
                author = row[2]
                summary = row[3]
                document = Document(id, title, author, summary)
                self._documents.append(document)
                document.tokenize()
                document.remove_stopwords() 
                document.normalize()
                document.lemmatize()

                for el in document.get_summary() :
                    if el in self._terms.keys() :
                        term = self._terms.get(el)
                    else :
                        term = Term(el)
                        self._terms[el] = term    
                    document.add_term(term)

                    term.add_doc(document)



    def get_all_documents(self) :
        return self._documents


    def get_all_terms(self) :
        return self._terms 

    





