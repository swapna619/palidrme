def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Predefined string
text = "hello"

# Check palindrome
if is_palindrome(text):
    print("The given string is a Palindrome")
else:
    print("The given string is NOT a Palindrome")
