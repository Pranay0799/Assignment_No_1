# Write a Python program that accepts a word from the user and reverse it.

word = input("Enter the word you want to reverse : ")
rev_word =""
i = len(word) - 1

while i >= 0:
    rev_word += word[i]
    i -= 1  
print(rev_word)


### Another method using for loop
# word = input("Enter the word you want to reverse : ")
# for i in word[::-1]:
#     print(i, end="")


#### Thank You....