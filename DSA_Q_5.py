### Q5. Write a recursive function to check if a given string is a palindrome.



str1 = input("Enter the string : ")  # "racecar"
def stringPalindrome(str1):
    if len(str1) > 1:
        return True
    if str1[0] == str1[-1]:
        return stringPalindrome(str1[1:-1])     
    else:
        return False    

# print(stringPalindrome(str1))
if print(stringPalindrome(str1)):
    print(f"{str1} is palindrome string.")
else:
     print(f"{str1} is not palindrome string.")









