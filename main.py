import re


def text(text, search):
    try:
        r = re.findall(f"{search}",text)
        print(len(r))
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        text(input("Text -->"), input("Search -->"))
    except Exception as e:
        print(f"Error {e}")
main()