# 3.Write a Python code to remove all characters except a           
# Sample String : 'exercises'
# Expected Result : 'eee' (Removed all characters except special character : e)

def remove_all_except(string, character):
    result = ''
    for char in string:
        if char == character:
            result += char
    return result
string = str(input("enter the string:"))
character = "a"
print("Sample String:", string)
print("Expected Result:", remove_all_except(string, character))

