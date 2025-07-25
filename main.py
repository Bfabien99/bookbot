import sys
from stats import get_book_text, get_num_words, character_occurence_in_text, reorganize_dict

arg = sys.argv
if len(arg) != 2 or arg[0] != 'main.py':
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    print("============ BOOKBOT ============")
    path = arg[1]
    print(f"Analyzing book found at {path}...")
    book_content = get_book_text(path)
    num_words = get_num_words(book_content)
    character_occurence = character_occurence_in_text(book_content)
    #print(character_occurence)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    new_list = reorganize_dict(character_occurence)

    for item in new_list :
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
    print("** created by bfabien99 for fun :-) **")

main()