

from InvertedIndex import *
from PhraseQuery import *
from SpellingCorrection import *
from Wilcard import Wilcard


class QueryParser :


    def assign_algorithm(self, query) :
        operators = ['AND', 'OR', 'NOT']
        print(query)
        if (self.check_wildcard(query)) :
            print('ho trovato una wildcard')
            return Wilcard()
        elif (self.check_operators(operators, query)) :   ### MANCANO LE WILCARDS ###
            return PhraseQuery()
        else :
            return InvertedIndex()


    def check_operators(self, operators, query) :
        for word in operators :
            if word in query :
                return False
        return True


    def check_wildcard(self, query) :
        for i in range(len(query)) :
            word = list(query[i])
            if '*' in word :
                return True
        return False

        
 
    



    