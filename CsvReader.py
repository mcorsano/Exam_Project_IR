
import csv
from Term import *
from Document import *


class CsvReader :


    def __init__(self, filename) -> None :
        self._filename = filename
        self._documents = {}
        self._terms = {}


    def read(self) :
        with open(self._filename, 'r', encoding="utf8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter = ';')
            for row in csv_reader :
                id = row[0]
                title = row[1]
                summary = row[2]
                document = Document(id, title, summary)
                self._documents[document.get_id()] = document
                document.tokenize()
                #document.remove_stopwords() 
                document.normalize()
                document.lemmatize()

                index = 0 
                for el in document.get_summary() :
                    if el in self._terms.keys() :
                        term = self._terms.get(el)
                        if term in document.get_terms().keys() :
                            document.add_term(term, index)
                        else :
                            document.add_new_term(term, index)
                            term.add_doc(document)
                    else :
                        term = Term(el)
                        self._terms[el] = term
                        document.add_new_term(term,index)

                        term.add_doc(document)
                    
                    index += 1  




    def get_all_documents(self) :
        return self._documents


    def get_all_terms(self) :
        return self._terms 

    





