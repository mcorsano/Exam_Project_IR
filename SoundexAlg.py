
from pyphonetics import RefinedSoundex 
rs = RefinedSoundex()


class SoundexAlg :


    def correct(self, word, all_words) :
        return [term for term in all_words if (rs.distance(word1=word, word2=term) == 0)]

