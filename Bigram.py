
from Term import *

class Bigram :


    def __init__(self, bigram) -> None:
        self._bigram = bigram
        self._terms = []


    def __str__(self) -> str :
        return str(self._bigram)


    def __repr__(self) -> str :
        return str(self)


    def add_term(self, term) :
        self._terms.append(term)
