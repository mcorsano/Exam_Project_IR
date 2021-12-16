
class PhraseQuery :


    def find(self, query, model) :
        terms = model.get_terms()
        text = []

        if (len(query) == 1) :
            # it means I am just looking for a single word
            # then I only need to return its posting list
            for posting in terms.get(query[0]).get_docs() :
                text.append(posting.short_description())
            if (len(text) == 1) :
                return 'The query is present in the following document:\n\n' + '\n'.join(text)
            else :
                return 'The query is present in the following documents:\n\n' + '\n'.join(text)

        documents = model.get_documents()
        query_words = query
        index = 0
        intermediate_dict = {}

        # when searching for multiple words, the phrase query retrieval algorithm is applied
        # to couple of terms at a time. Then, the intersection of results is returned
        while (index < len(query_words)-1) :
            word1 = query_words[index]
            word2 = query_words[index+1]
            term1 = terms.get(word1)
            term2 = terms.get(word2)

            posting_l1 = term1.get_posting_list()
            posting_l2 = term2.get_posting_list()

            i = 0
            j = 0
            # first I need to find the documents in common in the two posting lists 
            while (i < len(posting_l1) and j < len(posting_l2)) :
                if (posting_l1[i] == posting_l2[j]) :
                    doc = documents.get(posting_l1[i])
                    positions_1 = doc.get_term_positions(term1)
                    positions_2 = doc.get_term_positions(term2)

                    k = 0
                    l = 0
                    # when I found one common document, I look into the position indexes
                    # if the two words are present subsiquently in the document, their position has to be contiguous 
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
                
            index += 1        

        # in a single document, when performing a query containing more than 2 terms, a subset of the query may appear
        # even if the complete query is not present in the document itself.
        # So, I only take as results the documents in which all the couple of terms in the query are present in the correct order.
        answer_to_query = {}
        for key in intermediate_dict.keys() :
            answer_to_query[key] = []
            values = intermediate_dict.get(key)
            for el in values :
                if self.find_next_n_consecutives(el, len(query) - 2, values) :
                    answer_to_query[key].append(el)
        
        result =  dict((k, answer_to_query[k]) for k in answer_to_query.keys() if (len(answer_to_query.get(k)) != 0))

        # to get a more meaningful and aestetic result
        for doc in result.keys():
            text.append(doc.short_description() + ' - position: ' + str(result.get(doc)))
        if (len(text) == 1) :
            return 'The retrieved document and the relative position of the query inside of the terms is:\n\n' + '\n'.join(text)
        else:
            return 'The retrieved documents and the relative position of the query inside each of them are:\n\n' + '\n'.join(text)


    def find_next_n_consecutives(self, number, n, list_to_check) :
        tmp = number
        for i in range(n) :
            tmp += 1
            if (tmp in list_to_check) :
                pass
            else :
                return False
        return True