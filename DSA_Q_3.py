### Q3. Write a program to check if two strings are a rotation of each other?

str1 = input("Enter 1st string : ")   #"PQRS"
str2 = input("Enter 2nd string : ")   #"RSPQ"

def rotating_string(str1, str2):
    if len(str1) == len(str2):
        concatestr1_str2 = str1 + str1
        if str2 in concatestr1_str2:
            return "strings are a rotation of each other"
        else:
            return "strings are not a rotation of each other"
    else:
        return f"{str1} and {str2} are not the same length"

print(rotating_string(str1, str2))





















