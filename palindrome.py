import sys

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def main():
    # Jenkins / Command-line execution
    if len(sys.argv) == 2:
        text = sys.argv[1]

    # Local interactive execution
    else:
        text = input("Enter a string: ")

    if is_palindrome(text):
        print("The given string is a Palindrome")
    else:
        print("The given string is NOT a Palindrome")

if __name__ == "__main__":
    main()
