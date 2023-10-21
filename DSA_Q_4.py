# Q4. Write a program to print the first non-repeated character from a string?




str1 = input("Enter the string : ")

def non_repeatChar(str1):
    char_countDict = {}
    
    for i in str1:
        if i in char_countDict:
            char_countDict[i] += 1
        else:
            char_countDict[i] = 1
    
    print(char_countDict)

    for j in str1:
        if char_countDict[j] == 1:
            return f"Non repeat first character is : {j}"
        
print(non_repeatChar(str1))




