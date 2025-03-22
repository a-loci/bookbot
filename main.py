#PY project
from stats import count_text_words


def get_book_text(file_path):
    with open(file_path, "r") as file:
        txt = file.read()
        return txt



def main():
    frankenstein = "books/frankenstein.txt"
    #grab_file=get_book_text(frankenstein)
    #print(f"Printing Mary Shelly's Frankenstein...\n{grab_file}")

    print(count_text_words(frankenstein))


main()
    