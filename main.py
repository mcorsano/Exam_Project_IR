
from BooleanRetrievalSystem import *
from InvertedIndex import *
from PhraseQuery import PhraseQuery


file_name = 'out_subset.csv'
retrieval_model = BooleanRetrievalSystem(file_name)
documents_query2 = retrieval_model.search('Gorin OR consists')


