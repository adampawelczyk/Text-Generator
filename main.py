from nltk.tokenize import WhitespaceTokenizer
from nltk import trigrams
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
            word = choice(list(markov_model.keys())).split(" ")
            while word[0].islower() or not word[0].isalpha():
                word = choice(list(markov_model.keys())).split(" ")
            sentence.append(word[0])
            sentence.append(word[1])
        else:
            if sentence[-1][-1] in ".,?":
                if len(sentence) < 5:
                    sentence = []
                    continue
                else:
                    return sentence
            else:
                next_word = predict_next_word(" ".join(sentence[-2:]))
                word = next_word
                sentence.append(word)


def tokenize_text(text):
    whitespace_tokenizer = WhitespaceTokenizer()

    return whitespace_tokenizer.tokenize(text)


def create_markov_model(text_tokens):
    trigrams_list = list(trigrams(text_tokens))
    trigrams_dict = defaultdict(list)
    markov_model = {}

    for trigram in trigrams_list:
        trigrams_dict[trigram[0] + ' ' + trigram[1]].append(trigram[2])

    for key in trigrams_dict.keys():
        markov_model[key] = Counter(trigrams_dict[key]).most_common()

    return markov_model


def read_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        file_content = file.read()

        return file_content


def print_sentences():
    for _ in range(10):
        print(*generate_sentence())


file_name = input()

file_content = read_file(file_name)
file_tokens = tokenize_text(file_content)
markov_model = create_markov_model(file_tokens)

print_sentences()
