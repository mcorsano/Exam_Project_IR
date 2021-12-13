
from Term import *
from InvertedIndex import *
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


class PhraseQuery :


    def find(self, query, documents, terms) :
        query_words = query#.split()
        index = 0
        intermediate_dict = {}

        while (index < len(query_words)-1) :
            word1 = lemmatizer.lemmatize(query_words[index].lower())
            word2 = lemmatizer.lemmatize(query_words[index+1].lower())
            term1 = terms.get(word1)
            term2 = terms.get(word2)

            posting_l1 = term1.get_posting_list()
            posting_l2 = term2.get_posting_list()

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
                            if (doc not in intermediate_dict.keys()) :
                                intermediate_dict[doc] = [positions_1[k]]
                            else :
                                intermediate_dict[doc].append(positions_1[k])
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
            #print(intermediate_dict)              ### PHRASE QUERIES DA SISTEMARE PERCHè PRENDE SOLO UNA OCCORRENZA IN UN SINGOLO DOC ###


                
            index += 1
        
        answer_to_query = {key: value for key, value in intermediate_dict.items() if (len(value) == (len(query_words) -1))}
        
        return answer_to_query
        

