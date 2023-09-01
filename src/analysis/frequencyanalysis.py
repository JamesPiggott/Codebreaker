from collections import Counter
from math import sqrt
import languagedigrams
import languagefrequencies


class FrequencyAnalysis:
    """
    Analyze cipher text for letter frequency and digram similarity
    """

    def __init__(self, filename=None, language=None):
        self.message = None
        self.filename = filename
        self.language = language
        self.open_text()

    def open_text(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        # Combine lines, remove special characters and numerals, and convert to lowercase
        cleaned_text = ''.join(line.strip() for line in lines)
        cleaned_text = ''.join(filter(str.isalpha, cleaned_text)).lower()
        self.message = cleaned_text

    def getLetterCount(self, message, alphabet):
        # Returns a dictionary with keys of single letters and values of the
        # count of how many times they appear in the message parameter.
        letterCount = {letter: 0 for letter in alphabet}

        for letter in message.upper():
            if letter in alphabet:
                letterCount[letter] += 1

        return letterCount

    def getFrequencyOrder(self, message, alphabet, etaoin):
        # Returns a string of the alphabet letters arranged in order of most
        # frequently occurring in the message parameter.

        # first, get a dictionary of each letter and its frequency count
        letterToFreq = self.getLetterCount(message, alphabet)

        # second, make a dictionary of each frequency count to each letter(s)
        # with that frequency
        freqToLetter = {}
        for letter in alphabet:
            if letterToFreq[letter] not in freqToLetter:
                freqToLetter[letterToFreq[letter]] = [letter]
            else:
                freqToLetter[letterToFreq[letter]].append(letter)

        # third, put each list of letters in reverse "ETAOIN" order, and then
        # convert it to a string
        for freq in freqToLetter:
            freqToLetter[freq].sort(key=etaoin.find, reverse=True)
            freqToLetter[freq] = ''.join(freqToLetter[freq])

        # fourth, convert the freqToLetter dictionary to a list of tuple
        # pairs (key, value), then sort them
        freqPairs = list(freqToLetter.items())
        freqPairs.sort(key=lambda x: x[0], reverse=True)

        # fifth, now that the letters are ordered by frequency, extract all
        # the letters for the final string
        freqOrder = []
        for freqPair in freqPairs:
            freqOrder.append(freqPair[1])

        return ''.join(freqOrder)

    # Calculate cosine similarity between the vectors
    def cosine_similarity(self, vector1, vector2):
        # Calculate the dot product of two vectors
        dot_product = sum(a * b for a, b in zip(vector1, vector2))

        # Calculate the magnitude (Euclidean norm) of each vector
        magnitude1 = sqrt(sum(a ** 2 for a in vector1))
        magnitude2 = sqrt(sum(b ** 2 for b in vector2))

        # Avoid division by zero
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0

        # Calculate cosine similarity
        similarity = dot_product / (magnitude1 * magnitude2)

        return similarity

    def englishFreqMatchScore(self):
        """
        Calculate how the frequency score matches with the 6 most and least popular characters.
        Thus, a score of 12 is considered a perfect match with the English language
        :return:
        """
        freqOrder = self.getFrequencyOrder(self.message, languagefrequencies.english_alphabet,
                                           languagefrequencies.english_etaoin)
        matchScore = 0
        # Find how many matches for the six most common letters there are.
        for commonLetter in languagefrequencies.english_etaoin[:6]:
            if commonLetter in freqOrder[:6]:
                matchScore += 1
        # Find how many matches for the six least common letters there are.
        for uncommonLetter in languagefrequencies.english_etaoin[-6:]:
            if uncommonLetter in freqOrder[-6:]:
                matchScore += 1
        return matchScore

    def spanishFreqMatchScore(self):
        freqOrder = self.getFrequencyOrder(self.message, languagefrequencies.spanish_alphabet,
                                           languagefrequencies.spanish_etaoin)
        matchScore = 0
        for commonLetter in languagefrequencies.spanish_etaoin[:6]:
            if commonLetter in freqOrder[:6]:
                matchScore += 1
        for uncommonLetter in languagefrequencies.spanish_etaoin[-6:]:
            if uncommonLetter in freqOrder[-6:]:
                matchScore += 1
        return matchScore

    def germanFreqMatchScore(self):
        freqOrder = self.getFrequencyOrder(self.message, languagefrequencies.german_alphabet,
                                           languagefrequencies.german_etaoin)
        matchScore = 0
        for commonLetter in languagefrequencies.german_etaoin[:6]:
            if commonLetter in freqOrder[:6]:
                matchScore += 1
        for uncommonLetter in languagefrequencies.german_etaoin[-6:]:
            if uncommonLetter in freqOrder[-6:]:
                matchScore += 1
        return matchScore

    def frenchFreqMatchScore(self):
        freqOrder = self.getFrequencyOrder(self.message, languagefrequencies.french_alphabet,
                                           languagefrequencies.french_etaoin)
        matchScore = 0
        for commonLetter in languagefrequencies.french_etaoin[:6]:
            if commonLetter in freqOrder[:6]:
                matchScore += 1
        for uncommonLetter in languagefrequencies.french_etaoin[-6:]:
            if uncommonLetter in freqOrder[-6:]:
                matchScore += 1
        return matchScore

    def italianFreqMatchScore(self):
        freqOrder = self.getFrequencyOrder(self.message, languagefrequencies.italian_alphabet,
                                           languagefrequencies.italian_etaoin)
        matchScore = 0
        for commonLetter in languagefrequencies.italian_etaoin[:6]:
            if commonLetter in freqOrder[:6]:
                matchScore += 1
        for uncommonLetter in languagefrequencies.italian_etaoin[-6:]:
            if uncommonLetter in freqOrder[-6:]:
                matchScore += 1
        return matchScore

    def dutchFreqMatchScore(self):
        freqOrder = self.getFrequencyOrder(self.message, languagefrequencies.dutch_alphabet,
                                           languagefrequencies.dutch_etaoin)
        matchScore = 0
        for commonLetter in languagefrequencies.dutch_etaoin[:6]:
            if commonLetter in freqOrder[:6]:
                matchScore += 1
        for uncommonLetter in languagefrequencies.dutch_etaoin[-6:]:
            if uncommonLetter in freqOrder[-6:]:
                matchScore += 1
        return matchScore

    def generate_sorted_letter_bigrams_with_frequencies(self):
        # Remove non-alphabetic characters and convert to lowercase
        text = ''.join(filter(str.isalpha, self.message)).lower()

        # Check if the text is long enough for bigrams
        if len(text) < 2:
            return {}

        # Generate letter bigrams
        bigrams = [text[i:i + 2] for i in range(len(text) - 1)]

        # Calculate bigram frequencies
        bigram_frequency = {}
        for bigram in bigrams:
            if bigram in bigram_frequency:
                bigram_frequency[bigram] += 1
            else:
                bigram_frequency[bigram] = 1

        # Sort bigrams by frequency in descending order
        sorted_bigrams = sorted(bigram_frequency.items(), key=lambda x: x[1], reverse=True)

        return sorted_bigrams

    def generate_observed_bigram_from_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                text = file.read()

            # Remove non-alphabetic characters and convert to lowercase
            text = ''.join(filter(str.isalpha, text)).lower()

            # Check if the text is long enough for bigrams
            if len(text) < 2:
                return {}

            # Generate letter bigrams
            bigrams = [text[i:i + 2] for i in range(len(text) - 1)]

            # Calculate bigram frequencies using Counter
            observed_bigram = Counter(bigrams)

            return observed_bigram

        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return {}

    def convert_bigram_frequencies_to_percentage(self, observed_bigram):
        total_bigrams = sum(observed_bigram.values())
        return {bigram: count / total_bigrams for bigram, count in observed_bigram.items()}


f1 = FrequencyAnalysis("text_samples/english_sample_text.txt", 'English')
f1.open_text()
print(f1.englishFreqMatchScore())

f1 = FrequencyAnalysis("text_samples/spanish_sample_text.txt", 'Spanish')
f1.open_text()
print(f1.spanishFreqMatchScore())

f1 = FrequencyAnalysis("text_samples/german_sample_text.txt", 'German')
f1.open_text()
print(f1.germanFreqMatchScore())

f1 = FrequencyAnalysis("text_samples/french_sample_text.txt", 'French')
f1.open_text()
print(f1.frenchFreqMatchScore())

f1 = FrequencyAnalysis("text_samples/italian_sample_text.txt", 'Italian')
f1.open_text()
print(f1.italianFreqMatchScore())

f1 = FrequencyAnalysis("text_samples/dutch_sample_text.txt", 'Dutch')
f1.open_text()
print(f1.dutchFreqMatchScore())


# Apply cosine similarity to language digrams
f1 = FrequencyAnalysis("text_samples/dutch_sample_text.txt", "Dutch")
observed_bigram = f1.generate_observed_bigram_from_file()
observed_percentage = f1.convert_bigram_frequencies_to_percentage(observed_bigram)

expected_frequencies_lower = {key.lower(): value for key, value in languagedigrams.dutch_digram.items()}
common_keys = observed_percentage.keys() & expected_frequencies_lower.keys()

observed_vector = [observed_percentage[key] for key in common_keys]
expected_vector = [expected_frequencies_lower[key] for key in common_keys]

# Calculate cosine similarity between the observed and expected vectors
similarity_score = f1.cosine_similarity(observed_vector, expected_vector)

# Print the similarity score
print(f"Cosine Similarity Score: {similarity_score}")
