from stats import char_counter, get_book_text, order_dic, word_counter


# Main return
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(text)
    char_dic = char_counter(text)
    ordered_list = order_dic(char_dic)
    #print(f"{num_words} words found in the document")
    #print(f"{char_dic}")
    print(f"{ordered_list}")

main()
