from stats import word_counter
from stats import get_book_text
from stats import char_counter
from stats import sort
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

a = sys.argv[1]

def main():
    text = get_book_text(a)
    sorted_list = sort(char_counter(text))
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {word_counter(text)} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if(i.isalpha()):
            print(f"{i}: {sorted_list[i]}")
    print("============= END ===============")


main()