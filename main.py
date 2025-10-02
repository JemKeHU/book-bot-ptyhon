from stats import get_words_count, get_char_count, pretty_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        print(file_content)
    return file_content

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    char_dict = pretty_report(get_char_count(filename))
    word_num = get_words_count(filename)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{filename}...")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")
    for dict in char_dict:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()