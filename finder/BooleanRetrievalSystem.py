
from finder.CsvReader import CsvReader
from model.Model import Model
from algorithm.QueryParser import QueryParser
from spelling.SoundexAlg import SoundexAlg
from spelling.SpellingCorrection import SpellingCorrection


class BooleanRetrievalSystem :


    def __init__(self, filename) -> None :
        self._filename = filename
        self._model = Model()

    
    def read_csv(self) :
        reader = CsvReader(self._filename)
        reader.read()
        self._model.set_documents(reader.get_all_documents()) 
        self._model.set_terms(reader.get_all_terms())
        self._model.set_trigrams(reader.get_all_trigrams())


    def search(self, query) : 
        sc = SpellingCorrection(query)
        query = sc.preprocess_query()
        spelling_alg = SoundexAlg()
        sc.correct_spell(self._model.get_terms(), spelling_alg)

        search_algorithm = QueryParser().assign_algorithm(query) 
 
        return search_algorithm.find(query, self._model)
