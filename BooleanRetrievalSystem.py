
from CsvReader import *

class BooleanRetrievalSystem :
    def __init__(self, filename) -> None:
        self._filename = filename

    def search(self, query, search_algorithm) :
        reader = CsvReader(self._filename)
        reader.read()
        documents = reader.get_all_documents()
        terms = reader.get_all_terms()

        print(search_algorithm.find(query, documents, terms))   #i documenti forse non servono