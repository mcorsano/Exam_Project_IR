
class Term :


    def __init__(self, term) -> None :
        self._term = term
        self._docs = []


    def __str__(self) -> str :
        return str(self._term)


    def __repr__(self) -> str :
        return str(self)


    def __eq__(self, other) -> bool :
        return isinstance(other, Term) and other._term == self._term


    def __gt__(self, other) -> bool :
        return isinstance(other, Term) and other._term < self._term


    def __hash__(self) -> int :
        return hash(self._term)


    def get_docs(self) :
        return self._docs


    def get_term(self) :
        return self._term


    def add_doc(self, document) :
        self._docs.append(document)


    def get_posting_list(self) :
        posting_list = []
        for doc in self._docs :
            posting_list.append(doc.get_id())
        return sorted(posting_list)


    def get_positional_index(self) :
        positional_index = {}
        posting_list = self._docs 
        for posting in posting_list :
            positional_index[posting] = posting.get_term_positions(self._term)      ### fix this ###



