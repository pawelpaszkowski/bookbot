from stats import count_words, count_characters, sort_dictionary
import sys

def get_book_test(file_path):
    with open(file_path) as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3  main.py <path_to_book>")
        sys.exit(1)
    text = get_book_test(sys.argv[1])
    num_words = count_words(text)
    counted_characters = count_characters(text)
    sorted_dictionary = sort_dictionary(counted_characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_dictionary:
        if dictionary["character"].isalpha():
            print(f"{dictionary['character']}: {dictionary['value']}")

    print("============= END ===============")

main()
