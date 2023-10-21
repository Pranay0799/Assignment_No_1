### Q8. Write a program to check if all the brackets are closed in a given code snippet.


def are_brackets_balanced(code):
    count = 0

    for char in code:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False

    return count == 0

code_snippet = input("Enter the code snippet: ")
if are_brackets_balanced(code_snippet):
    print("Brackets are balanced.")
else:
    print("Brackets are not balanced.")
