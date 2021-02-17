from nltk.tokenize import WhitespaceTokenizer


file_name = input()

with open(file_name, encoding='utf-8') as file:
    file_content = file.read()
    whitespace_tokenizer = WhitespaceTokenizer()
    file_tokens = whitespace_tokenizer.tokenize(file_content)

    print("Corpus statistics")
    print(f"All tokens: {len(file_tokens)}")
    print(f"Unique tokens: {len(set(file_tokens))}")
    print()

    while True:
        try:
            index = input()
            if index == "exit":
                exit(0)
            index = int(index)

            if index > len(file_tokens) - 1:
                print("Index error. Please input an integer that is in the range of the corpus.")
            else:
                print(file_tokens[index])

        except ValueError:
            print("Type Error. Please input an integer.")
