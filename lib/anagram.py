# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        anagrams = []
        for possible_anagram in possible_anagrams:
            if self.is_anagram(possible_anagram):
                anagrams.append(possible_anagram)
        return anagrams

    def is_anagram(self, possible_anagram):
        return sorted(self.word) == sorted(possible_anagram.lower()) and self.word != possible_anagram.lower()
