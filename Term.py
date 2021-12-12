
class Term :


    def __init__(self, term) -> None :
        self._term = term
        self._docs = []


    def __str__(self) -> str :
        return str(self._term)


    def __repr__(self) -> str :
        return str(self)


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


    