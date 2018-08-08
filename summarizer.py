import re
import math
import nltk
import os
import string
import time
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
from operator import itemgetter


# WIP #

word = re.compile(r'\w+')


def sentence_to_vector(text):
    words = word.findall(text)
    return Counter(words)


def get_cosine(vec1, vec2):

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def summarize(data, value=0.20, language='english'):

    # all words that are irrelevant to sentence-vector/cosine-sim
    stop = list(set(stopwords.words(language))) + list(string.punctuation)
    # stemmer that stems all words for better cosine-sim calculation
    stemmer = SnowballStemmer(language)

    sentence_data = nltk.sent_tokenize(data)
    # initializes scores
    scores = [0 for sentence in sentence_data]

    for sentence_1 in sentence_data:

        cosines = []

        for sentence_2 in sentence_data:

            if sentence_2 is not sentence_1:
                # converts sentences into sentence-vectors with stemming
                # and stopwords removed
                sentence_1_list = [stemmer.stem(word) for word in
                                   word_tokenize(sentence_1.lower())
                                   if word not in stop]
                sentence_1 = ' '.join(sentence_1_list)
                sentence_1_vector = sentence_to_vector(sentence_1)
                sentence_2_list = [stemmer.stem(word) for word in
                                   word_tokenize(sentence_2.lower())
                                   if word not in stop]
                sentence_2 = ' '.join(sentence_2_list)
                sentence_2_vector = sentence_to_vector(sentence_2)
                cosine = get_cosine(sentence_1_vector, sentence_2_vector)
                cosines.append(cosine)

        cosines_ranked = sorted(cosines, reverse=True)

        # gives points to sentences based on location in ranked_scores
        for i in range(1, 5):
            cosine = cosines_ranked[i - 1]
            scores[cosines.index(cosine)] += 1 / i

    scores_ranked = sorted(scores, reverse=True)
    # amount of sentences in summary
    n = int(len(sentence_data) * value)

    sentences = []

    # adds sentences that have highest scores to our summarizations
    for i in range(n):

        sentence = sentence_data[scores.index(scores_ranked[i])]
        # skips over sentences that are already in summarization
        if sentence in [sentence[0] for sentence in sentences]:
            i -= 1
            continue
        sentences.append((sentence, sentence_data.index(sentence)))

    # sorts sentences based on their location in original text
    sentences.sort(key=itemgetter(1))
    return ' '.join([sentence[0] for sentence in sentences])


def main():

    for file in os.listdir('wikipedia-articles'):
        if file.endswith('.txt'):
            summarize_name = os.path.splitext(file)[0]
            with open('wikipedia-articles/' + str(file), 'r') as f:
                summarization = summarize(f.read())
                with open('wikipedia-summarizations/' + str(summarize_name) +
                          '-summarization.txt', 'w') as r:
                    r.write(summarization)


if __name__ == '__main__':
    main()
