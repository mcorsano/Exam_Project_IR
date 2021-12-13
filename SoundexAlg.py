
from pyphonetics import RefinedSoundex 
rs = RefinedSoundex()


class SoundexAlg :


    def correct(self, word, all_words) :
        suggestions = []
        for i in range(len(all_words)) :
            if (self.get_soundex(word) == self.get_soundex(all_words[i])) :
                suggestions.append(all_words[i])
        return suggestions

        #return [term for term in all_words if (rs.distance(word1=word, word2=term) == 0)]


    def get_soundex(self, name):
        name = name.upper()

        soundex = ""
        soundex += name[0]

        dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}

        for char in name[1:]:
            for key in dictionary.keys():
                if char in key:
                    code = dictionary[key]
                    if code != soundex[-1]:
                        soundex += code

        soundex = soundex.replace(".", "")
        soundex = soundex[:4].ljust(4, "0")

        return soundex