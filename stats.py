def get_word_count(book_text):
    count = 0
    for word in book_text.split():
        count += 1
    return count

def get_character_count(book_text):
    book_char_count = {}
    for word in book_text.split():
        for letter in word:
            if letter.lower() not in book_char_count:
                book_char_count[letter.lower()] = 1
            else:
                book_char_count[letter.lower()] += 1
    return book_char_count

def sorted_dictionary(char_count_dictionary):
    char_count_list = []
    for key, value in char_count_dictionary.items():
        char_count_list.append({"char": key, "num": value})
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list
   
   
def sort_on(d):
    return d["num"]

