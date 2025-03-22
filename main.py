#PY project
from stats import *
import sys



def get_book_text(file_path):
    with open(file_path, "r") as file:
        txt = file.read()
        return txt



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]  # Get path from command line
    frankenstein = get_book_text(book_path)

    #read_file=get_book_text(frankenstein)
    #print(f"Printing Mary Shelly's Frankenstein...\n{read_file}")

    organize= count_char(frankenstein)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(count_text_words(frankenstein))
    print("--------- Character Count -------")
    sort_dict(organize)


main()
    