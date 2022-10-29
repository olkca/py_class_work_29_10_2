def text(text):
    try:
        var = 0
        for t in text:
            if t.isdigit():
                var+=1
        print(f"Num -->{var}, Text -->{len(text)}, Letters -->{(len(text) - var)}")
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        text(input("Text -->"))
    except Exception as e:
        print(f"Error {e}")
main()