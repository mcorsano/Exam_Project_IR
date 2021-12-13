

from InvertedIndex import *
from PhraseQuery import *
from SpellingCorrection import *


class QueryParser :


    def assign_algorithm(self, query) :
        operators = ['AND', 'OR', 'NOT']
        if (self.check_operators(operators, query)) :   ### MANCANO LE WILCARDS ###
            return PhraseQuery()
        else :
            return InvertedIndex()


    def check_operators(self, operators, query) :
        for word in operators :
            if word in query :
                return False
        return True
        
 
    



    