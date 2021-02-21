from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import defaultdict, Counter
from random import choices, choice


def predict_next_word(word):
    list_of_tails = [x[0] for x in markov_model[word]]
    tails_occurrence_count = [x[1] for x in markov_model[word]]

    return choices(list_of_tails, tails_occurrence_count)[0]


def generate_sentence():
    sentence = list()

    while True:
        if len(sentence) == 0:
            word = choice(list(markov_model.keys()))
            while word[0].islower() or not word[0].isalpha():
                word = choice(list(markov_model.keys()))
            sentence.append(word)
        else:
            if sentence[-1][-1] in ".,?":
                if len(sentence) < 5:
                    sentence = []
                    continue
                else:
                    return sentence
            else:
                next_word = predict_next_word(word)
                word = next_word
                sentence.append(word)


file_name = input()

with open(file_name, encoding='utf-8') as file:
    file_content = file.read()
    whitespace_tokenizer = WhitespaceTokenizer()
    file_tokens = whitespace_tokenizer.tokenize(file_content)
    bigrams = list(bigrams(file_tokens))
    bigrams_dict = defaultdict(list)
    markov_model = {}

    for bigram in bigrams:
        bigrams_dict[bigram[0]].append(bigram[1])

    for key in bigrams_dict.keys():
        markov_model[key] = Counter(bigrams_dict[key]).most_common()

    for _ in range(10):
        print(*generate_sentence())
