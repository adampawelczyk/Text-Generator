from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import defaultdict, Counter
from random import choices, choice


def predict_next_word(word):
    list_of_tails = [x[0] for x in markov_model[word]]
    tails_occurrence_count = [x[1] for x in markov_model[word]]

    return choices(list_of_tails, tails_occurrence_count)[0]


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

    first_word = choice(list(markov_model.keys()))

    sentences = list()
    sentences.append(first_word)
    next_word = predict_next_word(first_word)

    for _ in range(99):
        next_word = predict_next_word(next_word)
        sentences.append(next_word)

    for i in range(len(sentences) // 10 + 1):
        print(" ".join(sentences[i * 10: (i + 1) * 10]))
