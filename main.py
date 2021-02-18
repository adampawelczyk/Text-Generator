from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams


file_name = input()

with open(file_name, encoding='utf-8') as file:
    file_content = file.read()
    whitespace_tokenizer = WhitespaceTokenizer()
    file_tokens = whitespace_tokenizer.tokenize(file_content)
    bigram = list(bigrams(file_tokens))

    print(f"Number of bigrams: {len(bigram)}")
    print()

    while True:
        try:
            index = input()
            if index == "exit":
                exit(0)
            index = int(index)

            if index > len(bigram) - 1:
                print("Index error. Please input an integer that is not greater that the number of all bigrams.")
            else:
                print(f"Head: {bigram[index][0]}\t\tTail: {bigram[index][1]}")

        except ValueError:
            print("Type Error. Please input an integer.")
