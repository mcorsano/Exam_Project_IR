
from Term import *
from InvertedIndex import *
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


class PhraseQuery :


    def find(self, query, documents, terms) :
        query_words = query.split()
        index = 0
        while (index < len(query_words)-1) :
            word1 = lemmatizer.lemmatize(query_words[index].lower())
            word2 = lemmatizer.lemmatize(query_words[index+1].lower())
            term1 = terms.get(word1)
            term2 = terms.get(word2)

            posting_l1 = term1.get_posting_list()
            posting_l2 = term2.get_posting_list()

            #intersection_posting_l = InvertedIndex().intersection(term1, term2)
           
            '''
            for posting in intersection_posting_l :
                doc = documents.get(posting)
                positions_1 = doc.get_term_positions(term1)
                positions_2 = doc.get_term_positions(term2)

                print(positions_1)
                print(positions_2)
            '''
            position_of_first = []
            i = 0
            j = 0
            while (i < len(posting_l1) and j < len(posting_l2)) :
                if (posting_l1[i] == posting_l2[j]) :
                    doc = documents.get(posting_l1[i])
                    positions_1 = doc.get_term_positions(term1)
                    positions_2 = doc.get_term_positions(term2)
                    k = 0
                    l = 0
                    while (k < len(positions_1) and l < len(positions_2)) :
                        if (positions_1[k] == (positions_2[l] - 1)) :
                            print('trovato')
                            position_of_first.append(positions_1[k])
                            k += 1
                            l += 1
                        elif (positions_1[k] < (positions_2[l] - 1)) :
                            k += 1
                        else :
                            l += 1
                    i += 1
                    j += 1
                elif (posting_l1[i] < posting_l2[j]) :
                    i += 1
                else :
                    j += 1
            print(position_of_first)


                
            index += 1
    
        return 'fine della query'
        

