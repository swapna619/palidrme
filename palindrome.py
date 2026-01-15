def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


if __name__ == "__main__":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("The string is a Palindrome")
    else:
        print("The string is NOT a Palindrome")
