from stats import get_word_count
from stats import get_character_count
from stats import sorted_dictionary
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        book = f.read()
        return book

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]
    #grabs text of book and assigns to variable as a string
    book_text = get_book_text(book)

    word_count = get_word_count(book_text)
    char_dict = get_character_count(book_text)
    char_count_list = sorted_dictionary(char_dict)


    #print("============ BOOKBOT ============")
    #print("Analyzing book found at books/frankenstein.txt...")
    #print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    #print("--------- Character Count -------")

    for item in char_count_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    #print("============= END ===============")




main()