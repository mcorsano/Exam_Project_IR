
from Term import *

class InvertedIndex :

    def find(self, query, documents, terms) :   # i documenti forse non servono
        words = query.split()
        term1 = terms.get(words[0])
        term2 = terms.get(words[2])
        operator = words[1]

        if (operator == 'AND') :
            return self.intersection(term1, term2)
        elif (operator == 'OR') :
            return self.union(term1, term2)
        elif (operator == 'NOT') :
            return self.difference(term1, term2)
        else :
            raise ValueError


    def intersection(self, term1, term2) :
        posting_l1 = term1.get_posting_list()
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



    def union(self, term1, term2) :
        posting_l1 = term1.get_posting_list()
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
                union_posting_l.append(posting_l2[posting_l2])
                j += 1

        if (i >= len(posting_l1)) :
            union_posting_l.extend(posting_l2[j:len(posting_l2)])
        if (j >= len(posting_l2)) :
            union_posting_l.extend(posting_l1[i:len(posting_l1)])

        return union_posting_l


   
    def difference(self, term1, term2) :
        posting_l1 = term1.get_posting_list()
        posting_l2 = term2.get_posting_list()
        difference_posting_l = []

        difference_posting_l = posting_l1.copy()
        for posting in posting_l2 :
            if posting in difference_posting_l :
                difference_posting_l.remove(posting)
        
        return difference_posting_l

