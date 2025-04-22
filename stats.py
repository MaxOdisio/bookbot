# Get a file and return its contents as a unique string
def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content

# Return the number of words in a string
def word_counter(content):
    splitted = content.split()
    num_words = len(splitted)
    return num_words

# Return the number of each character in a string
def char_counter(content):
    char_list= {}
    for char in content:
        low_char = char.lower()
        if low_char in char_list:
            char_list[low_char] = char_list[low_char] + 1
        else:
            char_list[low_char] = 1
    return char_list
