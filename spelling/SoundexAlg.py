
class SoundexAlg :


    def correct(self, word, all_words) :
        suggestions = []
        for i in range(len(all_words)) :
            if (self.get_soundex(word) == self.get_soundex(all_words[i])) :
                suggestions.append(all_words[i])
        return suggestions
        

    def get_soundex(self, word):
        word = word.upper()
        soundex = word[0]
        dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}

        for char in word[1:]:
            for key in dictionary.keys():
                if char in key:
                    code = dictionary[key]
                    if code != soundex[-1]:
                        soundex += code

        soundex = soundex.replace(".", "")
        soundex = soundex[:4].ljust(4, "0")

        return soundex