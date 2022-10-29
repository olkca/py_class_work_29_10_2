import re


def text(text, search_word):
    try:
        r = re.findall(search_word,text)
        print(len(r))
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        text(input("Text -->"), input("Search -->"))
    except Exception as e:
        print(f"Error {e}")
main()