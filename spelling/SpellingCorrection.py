
import re
from nltk.stem import WordNetLemmatizer
from algorithm.Wildcard import Wildcard


class SpellingCorrection :


    def __init__(self, query) -> None:
        self._query = query


    def preprocess_query(self) :
        exceptions = ['AND', 'NOT', 'OR']
        query = re.sub(r'[^\w\s\\*]','', self._query)
        final_query = []
        lemmatizer = WordNetLemmatizer()
        for word in query.split() :
            if word in exceptions :
                final_query.append(word)
            else :
                final_query.append(lemmatizer.lemmatize(word.lower()))   
        return final_query


    def correct_spell(self, all_terms, spelling_alg) :
        query = self._query.split()
        if (Wildcard.has_wildcard(query)) :
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
                    raise ValueError('The inserted word is not present, please refrase the query.\n\nPossible suggestions:\n' + ' '.join([str(elem) for elem in possible_corrections]))
            return query
 