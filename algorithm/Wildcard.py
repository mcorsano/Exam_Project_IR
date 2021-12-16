
class Wildcard :


    def find(self, query, model) :
        trigrams = model.get_trigrams()
        trigram_dict = trigrams
        answer = []
        word = query[0]
        word = list(word)
        word = ''.join([str(letter) for letter in word])
        trigrams = self.get_trigrams(word)
        answer.extend(self.find_terms_containing(trigrams, trigram_dict))
        if (len(answer) == 1) :
            return 'The resulting answer to the given wildcard query is: \n\n' + ', '.join(answer)
        else :
            return 'The resulting answers to the given wildcard query are: \n\n' + ', '.join(answer)


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
            else :
                raise ValueError('The current research lead to no results.\nPlease, refrase a new query')
        return set(answer)

    @staticmethod
    def has_wildcard(query) :
        for i in range(len(query)) :
            word = list(query[i])
            if '*' in word :
                return True
        return False
        
