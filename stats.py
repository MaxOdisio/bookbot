# Get a file and return its contents as a unique string
def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content

# Return the number of words
def word_counter(content):
    splitted = content.split()
    num_words = len(splitted)
    return num_words
