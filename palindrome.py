# palindrome_check.py
# Program to check whether a string is a palindrome

import sys

def is_palindrome(text):
    """Function to check palindrome"""
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]


if __name__ == "__main__":
    print("\n---- Palindrome Checker ----\n")
    try:
        # Case 1: Argument passed (for Jenkins or CLI)
        if len(sys.argv) == 2:
            text = sys.argv[1]

        # Case 2: No argument passed (for console use)
        else:
            text = input("Enter a string: ")

        result = is_palindrome(text)

        print(f"\nInput Text: {text}")
        if result:
            print("Result: The given string is a Palindrome\n")
        else:
            print("Result: The given string is NOT a Palindrome\n")

    except Exception as e:
        print("Error occurred:", e)
