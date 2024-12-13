

import string

def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_path(book_path)
    num_words = count_words(text)
    print(f"Number of words in the book: {num_words}")
    num_letters = count_letters(text)
    report(num_letters)

def get_book_path(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    dict_letters = {}  
    for x in string.ascii_lowercase:
        dict_letters.update({x: 0})

    mystring = text
    lower_string = mystring.lower()
    for letter in lower_string:
        if letter in dict_letters:
            existing_count = dict_letters[letter]
            existing_count += 1
            dict_letters[letter] = existing_count
    return dict_letters

def report(dictionary):
    for i in dictionary:
        print(f"The '{i}' character was found {dictionary[i]}")

main()
