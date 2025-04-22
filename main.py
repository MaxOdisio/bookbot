from stats import get_book_text, word_counter


# Main return
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(text)
    print(f"{num_words} words found in the document")

main()
