def main():
    PATH = "books/frankenstein.txt"
    frankenstein_content = open_book_content(PATH)

    print(f"---Begin report of {PATH}---")
    word_count = get_words_count(frankenstein_content)
    print(f"{word_count} words was found in the document")
    char_dict = get_characters_count(frankenstein_content)
    char_dict_list = convert_dict_to_list(char_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    print(char_dict_list)
    for char_dict in char_dict_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")

def open_book_content(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_words_count(text):
    words = text.split()
    return len(words)

def get_characters_count(texts):
    words = texts.split()
    words_string = "".join(words)
    char_dict = {}
    for char in words_string:
        char = char.lower()
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    new_list = []
    for k,v in dict.items():
        temp_dict = {"char":k, "num":v}
        new_list.append(temp_dict)
    return(new_list)


main()
