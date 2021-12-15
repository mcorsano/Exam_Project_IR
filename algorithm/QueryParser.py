

from algorithm.InvertedIndex import *
from algorithm.PhraseQuery import *
from algorithm.Wildcard import *


class QueryParser :


    def assign_algorithm(self, query) :
        operators = ['AND', 'OR', 'NOT']
        if (Wildcard.has_wildcard(query)) :
            return Wildcard()
        elif (self.has_not_operators(operators, query)) : 
            return PhraseQuery()
        else :
            return InvertedIndex()


    def has_not_operators(self, operators, query) :
        for word in operators :
            if word in query :
                return False
        return True
