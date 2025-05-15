def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def word_counter(text):
    words = text.split()
    count = 0
    for i in words:
        count += 1 
    return count

def char_counter(text):
    char_list = []
    char_count = {}
    for i in text:
        char_list.append(i.lower())
    for char in char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort(d):
    items = list(d.items())
    items.sort(reverse=True,key=lambda i: i[1])
    sd = dict(items)
    return sd