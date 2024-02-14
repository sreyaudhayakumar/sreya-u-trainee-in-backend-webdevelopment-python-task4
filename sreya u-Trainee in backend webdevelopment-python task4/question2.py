# 2.Print even length words in a string.
# Sample String : ''I love coding"
# Expected Result : “love, coding”

def print_even_length(string):
    words = string.split()
    even_length_words = [word for word in words if len(word) % 2 == 0]
    result = ", ".join(even_length_words)
    return result

user_input=str(input("enter the string:"))
print(" String:", user_input)
print(" Result:", print_even_length(user_input))
