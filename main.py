def text(text, search, word):
    try:
        r = text.replace (search, word)
        print(r)
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        text(input("Text -->"), input("Search -->"), input("Word -->"))
    except Exception as e:
        print(f"Error {e}")
main()