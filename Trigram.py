
from Term import *

class Trigram :


    def __init__(self, trigram) -> None:
        self._trigram = trigram
        self._terms = []


    def __str__(self) -> str :
        return str(self._trigram)


    def __repr__(self) -> str :
        return str(self)


    def add_term(self, term) :
        self._terms.append(term)
