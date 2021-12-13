
from BooleanRetrievalSystem import *
from InvertedIndex import *
from PhraseQuery import PhraseQuery


file_name = 'corpus.csv'
retrieval_model = BooleanRetrievalSystem(file_name)
#documents_query1 = retrieval_model.search('Pino OR otter', InvertedIndex()) # BooleanRetrieval()) 
documents_query2 = retrieval_model.search('Pino OR really')# years bear')#, PhraseQuery())


