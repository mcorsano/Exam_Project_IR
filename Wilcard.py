
from Bigram import *


class Wilcard :


    def find(self, query, documents, all_terms) :
        trigram_dict = self.generate_trigrams_dict(all_terms)
        answer = []
        word = query[0]
        word = list(word)
        word = ''.join([str(letter) for letter in word])
        trigrams = self.get_trigrams(word)
        answer.extend(self.find_terms_containing(trigrams, trigram_dict))
        return answer


    def generate_trigrams_dict(self, all_terms) :
        trigram_dict = {}
        for term in all_terms.keys() :
            trigrams = self.get_trigrams(term)
            for tri in trigrams :
                if tri in trigram_dict.keys() :
                    trigram_dict[tri].append(all_terms.get(term))
                else :
                    #bi = Bigram(term)
                    trigram_dict[tri] = [all_terms.get(term)]
        return trigram_dict


    def get_trigrams(self, term) :
        trigrams = []
        word = '$$' + term + '$$'
        word = [c for c in word]
        for i in range(len(word) - 2) :
            tri = word[i:i+3]
            if ('*' not in tri) :
                trigrams.append(''.join([str(letter) for letter in tri]))
        return trigrams


    def find_terms_containing(self, trigrams, trigram_dict) :
        answer = trigram_dict.get(trigrams[0])
        for tri in trigrams :
            if tri in trigram_dict.keys() :
                answer = [t for t in trigram_dict.get(tri) if t in answer]   #intersection of lists of terms 
            #else :
                #print('trigram not found')
        return answer


    
        
