import sys

from stats import char_counter, get_book_text, order_dic, word_counter


# Main return
def main(file):
    text = get_book_text(file)
    num_words = word_counter(text)
    char_dic = char_counter(text)
    ordered_list = order_dic(char_dic)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for element in ordered_list:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
