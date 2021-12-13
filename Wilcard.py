
class Wilcard :


    def find(self, query, documents, terms) :
        word = query[0]
        word = list(word)
        if (word[0] == '*') :
            print('leading wildcard')
        elif (word[-1] == '*') :
            print('trailing wilcard')
        else :
            print('mid wildcard')
        #term = terms.get(word)
        #print(term.get_posting_list())