
from Bigram import *


class Wilcard :


    def find(self, query, documents, all_terms) :
        bigram_dict = self.generate_bigrams_dict(all_terms)
        answer = []
        word = query[0]
        word = list(word)
        word = ''.join([str(letter) for letter in word])
        bigrams = self.get_bigrams(word)
        answer.extend(self.find_terms_containing(bigrams, bigram_dict))
        return answer


    def generate_bigrams_dict(self, all_terms) :
        bigram_dict = {}
        for term in all_terms.keys() :
            bigrams = self.get_bigrams(term)
            for bi in bigrams :
                if bi in bigram_dict.keys() :
                    bigram_dict[bi].append(all_terms.get(term))
                else :
                    #bi = Bigram(term)
                    bigram_dict[bi] = [all_terms.get(term)]
        return bigram_dict


    def get_bigrams(self, term) :
        bigrams = []
        word = '$' + term + '$'
        word = [c for c in word]
        for i in range(len(word) - 1) :
            bi = word[i:i+2]
            if ( '*' not in bi) :
                bigrams.append(''.join([str(letter) for letter in bi]))
        return bigrams


    def find_terms_containing(self, bigrams, bigram_dict) :
        answer = bigram_dict.get(bigrams[0])
        #print(answer)
        for bi in bigrams :
            if bi in bigram_dict.keys() :
                #print(bigram_dict[bi])
                answer = [t for t in bigram_dict.get(bi) if t in answer]   #intersection of lists of terms 
            else :
                print('there is something weird going on, mate...')
        return answer


    
        
