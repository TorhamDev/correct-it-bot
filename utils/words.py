def load_words_file(file_path: str) -> set:
    with open(file_path, "r") as file:
        return {line.strip() for line in file}


words = load_words_file("utils/words.txt")


def update_words_file(file_path: str) -> None:
    with open(file_path, "w") as file:
        for word in words:
            file.write(f"{word}\n")


def add_sentence_words(sentence: str) -> None:
    new_words = set(sentence.replace("!add", "", 1).split())
    print(f"These new wrods are going to add: {new_words}")
    for word in new_words:
        words.add(word)
    
    update_words_file("utils/words.txt")
