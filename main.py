from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import defaultdict, Counter


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

    while True:
        index = input()
        if index == "exit":
            exit(0)

        print(f"Head: {index}")

        if index in markov_model:
            for item in markov_model[index]:
                print(f"Head: {item[0]}\t\tTail: {item[1]}")
        else:
            print("Key Error. The requested word is not in the model. Please input another one")

        print()
