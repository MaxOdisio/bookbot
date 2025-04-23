from stats import char_counter, get_book_text, order_dic, word_counter


# Main return
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(text)
    char_dic = char_counter(text)
    ordered_list = order_dic(char_dic)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for element in ordered_list:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")

main()
