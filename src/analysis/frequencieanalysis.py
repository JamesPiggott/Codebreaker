"""
Analyze cipher text for letter frequency to determine language used
"""

class FrequencieAnalysis:

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

    def __init__(self, filename, language):
        self.filename = filename
        self.language = language
        self.message = self.open_text()

    def open_text(self):
        file = open(self.filename, 'r')
        Lines = file.readlines()

        text = ""
        for line in Lines:
            line = line.strip()
            text += line

        return text

    def letter_count(self):
        lettercount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
            'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
            'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
            'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

        for letter in self.message.upper():
            if letter in self.LETTERS:
                lettercount[letter] += 1

        return lettercount

    def frequency_order(self):
        # Get a dictionary of each letter and their count
        letterToFreq = self.letter_count()
        # Make a dictionary of each frequency count to the letter(s)
        freqToLetter = {}
        for letter in self.LETTERS:
            if letterToFreq[letter] not in freqToLetter:
                freqToLetter[letterToFreq[letter]] = [letter]
            else:
                freqToLetter[letterToFreq[letter]].append(letter)

        # Put each of the letters in reverse "ETAOIN" order and convert to string
        for freq in freqToLetter:
            freqToLetter[freq].sort(key=self.ETAOIN.find, reverse=True)
            freqToLetter[freq] = ''.join(freqToLetter[freq])

        # # Convert the freqToLetter dictionary to a list of tuple pairs and sort
        freqPairs = list(freqToLetter.items())
        freqPairs.sort(key=freqToLetter[0], reverse=True)
        #
        # # Letters sorted by frequency, now turn to string
        # freqOrder = []
        # for freqPair in freqPairs:
        #     freqOrder.append(freqPair[1])

        # return ''.join(freqToLetter)
        return freqToLetter

f1 = FrequencieAnalysis("sample_text.txt", 'English')

f1.open_text()

order = f1.frequency_order()

print(order)