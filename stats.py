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

# Return a dictionary with number of each character in a string
def char_counter(content):
    char_list= {}
    for char in content:
        low_char = char.lower()
        if low_char in char_list:
            char_list[low_char] = char_list[low_char] + 1
        else:
            char_list[low_char] = 1
    return char_list

# Return an ordered list of dictionaries
def order_dic(dic):
    new_list = []
    for key in dic:
        value = dic[key]
        new_dic = {}
        new_dic["char"] = key
        new_dic["num"] = value
        new_list.append(new_dic)
    def sort_on(d):
        return d["num"]
    new_list.sort(reverse=True, key=sort_on)
    return new_list
