
class PostingList :

    def __init__(self, term) -> None:
        self._term = term
        self._posting_list = []

    
    def __copy__(self):
        new_pl = PostingList(self._term)
        return new_pl

    
    def __len__(self) :
        return len(self._posting_list)


    def __eq__(self, other) :
        return isinstance(other, PostingList) and other._posting_list == self._posting_list


    def add_doc(self, doc) :
        self._posting_list.append(doc.get_id)
        