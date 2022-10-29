import re


def text(text, search_symbol):
    try:
        r = re.findall(f"{search_symbol}",text)
        print(len(r))
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        text(input("Text -->"), input("Search -->"))
    except Exception as e:
        print(f"Error {e}")
main()