
from BooleanRetrievalSystem import *
from InvertedIndex import *


file_name = 'corpus.csv'
retrieval_model = BooleanRetrievalSystem(file_name)
documents = retrieval_model.search('Pino NOT otter', InvertedIndex()) # BooleanRetrieval()) 



