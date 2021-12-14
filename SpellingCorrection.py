
import re
from SoundexAlg import *
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


class SpellingCorrection :


    def normalize_query(self, query) :
        exceptions = ['AND', 'NOT', 'OR']
        query = re.sub(r'[^\w\s\\*]','', query)
        final_query = []
        for word in query.split() :
            if word in exceptions :
                final_query.append(word)
            else :
                final_query.append(lemmatizer.lemmatize(word.lower()))   
        return final_query


    def correct_spell(self, all_terms, query, spelling_alg) :
        if (self.check_wildcard(query)) :
            return query
        else:               
            all_words = list(all_terms.keys())
            all_words.extend(['AND', 'NOT', 'OR'])
            for i in range(len(query)) :
                possible_corrections = []
                if query[i] in all_words :
                    pass
                else :
                    possible_corrections.extend(spelling_alg.correct(query[i], all_words))
                    #print('the inserted word is not present, substitute it with a different one ', possible_corrections, '?')
                    raise ValueError('The inserted word is not present, please refrase the query.\nDid you mean one of these?\n' + ' '.join([str(elem) for elem in possible_corrections]))
                    #correct_word = input()
                    #query[i] = correct_word
            return query



    def check_wildcard(self, query) :
        for i in range(len(query)) :
            word = list(query[i])
            if '*' in word :
                return True
        return False
                





        



    

