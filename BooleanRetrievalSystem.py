
from re import search
from CsvReader import *
from PhraseQuery import *
from Wilcard import *
from QueryParser import QueryParser
from SoundexAlg import SoundexAlg
from SpellingCorrection import SpellingCorrection



class BooleanRetrievalSystem :


    def __init__(self, filename) -> None :
        self._filename = filename
        self._documents = {}
        self._terms = {}
        self._trigrams = {}

    
    def read_csv(self) :
        reader = CsvReader(self._filename)
        reader.read()
        self._documents = reader.get_all_documents()
        self._terms = reader.get_all_terms()
        self._trigrams = reader.get_all_trigrams()


    def search(self, query) : 
        sc = SpellingCorrection()
        query = sc.preprocess_query(query)
        spelling_alg = SoundexAlg()
        sc.correct_spell(self._terms, query, spelling_alg)       

        search_algorithm = QueryParser().assign_algorithm(query) 
 
        return search_algorithm.find(query, self._documents, self._terms, self._trigrams)     ### add self._trigrams ###


    
