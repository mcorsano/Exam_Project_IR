
from Term import *
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


class InvertedIndex :


    def find(self, query, documents, terms) :   # i documenti forse non servono
        words = query

        word1 = words[0]
        previous_pl = terms.get(word1).get_posting_list()
        for i in range(1, len(query), 2) :
            word2 = words[i+1]
            term2 = terms.get(word2)
            operator = words[i]

            if (operator == 'AND') :
                answer = self.intersection(previous_pl, term2)
            elif (operator == 'OR') :
                answer = self.union(previous_pl, term2)
            elif (operator == 'NOT') :
                answer = self.difference(previous_pl, term2)
            else :
                raise ValueError
        
            previous_pl = answer
            
        return answer


    def intersection(self, posting_l1, term2) :
        posting_l2 = term2.get_posting_list()
        intersection_posting_l = []
      
        i = 0
        j = 0
        while (i < len(posting_l1) and j < len(posting_l2)) :
            if (posting_l1[i] == posting_l2[j]) :
                intersection_posting_l.append(posting_l1[i])
                i += 1
                j += 1
            elif (posting_l1[i] < posting_l2[j]) :
                i += 1
            else :
                j += 1

        return intersection_posting_l


    def union(self, posting_l1, term2) :
        posting_l2 = term2.get_posting_list()
        union_posting_l = []

        i = 0
        j = 0
        while (i < len(posting_l1) and j < len(posting_l2)) :
            if (posting_l1[i] == posting_l2[j]) :
                union_posting_l.append(posting_l1[i])
                i += 1
                j += 1
            elif (posting_l1[i] < posting_l2[j]) :
                union_posting_l.append(posting_l1[i])
                i += 1
            else :
                union_posting_l.append(posting_l2[j])
                j += 1

        if (i >= len(posting_l1)) :
            union_posting_l.extend(posting_l2[j:len(posting_l2)])
        if (j >= len(posting_l2)) :
            union_posting_l.extend(posting_l1[i:len(posting_l1)])

        return union_posting_l

   
    def difference(self, posting_l1, term2) :
        posting_l2 = term2.get_posting_list()
        difference_posting_l = []

        difference_posting_l = posting_l1.copy()
        for posting in posting_l2 :
            if posting in difference_posting_l :
                difference_posting_l.remove(posting)
        
        return difference_posting_l

  