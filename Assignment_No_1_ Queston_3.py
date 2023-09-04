# Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9

odd_count = 0
even_count = 0

for i in numbers:
    if i%2 ==1:
        odd_count += 1
    else:
        even_count += 1

print("Number of even numbers : ", even_count)
print("Number of odd numbers : ", odd_count)


#### Thank You....

