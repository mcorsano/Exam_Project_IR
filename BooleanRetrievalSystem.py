
from re import search
from CsvReader import *
from PhraseQuery import *
from QueryParser import QueryParser
qp = QueryParser()
from SoundexAlg import SoundexAlg
from SpellingCorrection import SpellingCorrection
sc = SpellingCorrection()



class BooleanRetrievalSystem :


    def __init__(self, filename) -> None :
        self._filename = filename

    def search(self, query) : #, search_algorithm) :
        reader = CsvReader(self._filename)
        reader.read()
        documents = reader.get_all_documents()
        terms = reader.get_all_terms()

        query = sc.normalize_query(query)
        spelling_alg = SoundexAlg()
        sc.correct_spell(terms, query, spelling_alg)       

        search_algorithm = qp.assign_algorithm(query) 
 
        #print(search_algorithm.find(query, documents, terms))

        return search_algorithm.find(query, documents, terms)


    
