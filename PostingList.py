
class PostingList :

    def __init__(self, term) -> None:
        self._term = term
        self._posting_list = sorted(term.get_posting_list())


    def __copy__(self):
        new_pl = PostingList(self._term)
        return new_pl

    
    def __len__(self) :
        return len(self._posting_list)


    def __eq__(self) :
        