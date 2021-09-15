dict = {"bear":"con gấu", "elephant":"con voi", "fox": "con cáo", "jaguar":"báo đốm", "lion":"sư tử", "raccoon":"gấu mèo"}

def input_data(text):
    return input(text)

def is_in_dict(text, dict):
    for key in dict:
        if key == text:
            return True
        else:
            return False

if __name__ == '__main__':
    word = input_data("Enter the word to be translated into Vietnamese: ")
    if is_in_dict(word, dict):
        print(f"'{word}' : '{dict[word]}'")
    else:
        print(f"'{word}' is not in English dictionary")