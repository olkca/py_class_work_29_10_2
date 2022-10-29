def text(a):
    try:
        return a[:: -1]
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        r = text(input("Text -->"))
        print(r)
    except Exception as e:
        print(f"Error {e}")
main()