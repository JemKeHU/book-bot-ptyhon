def get_words_count(filepath):
    with open(f"{filepath}") as f:
        words_list = f.read().split()
        words_count = len(words_list)
    return words_count

def get_char_count(filepath):
    with open(f"{filepath}") as f:
        char_count = {}
        file_content = f.read()
        for char in file_content:
            lowered = char.lower()
            if lowered not in char_count:
                char_count[lowered] = 1
            else:
                char_count[lowered] += 1
        return char_count
    
def sort_by_num(items):
    return items["num"]

def pretty_report(char_dict):
    char_list = []
    for key in char_dict:
        char_list.append({"char": key, "num": char_dict[key]})
    char_list.sort(reverse=True, key=sort_by_num)
    return char_list