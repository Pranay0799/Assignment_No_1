# Write a Python program to count the number of even and odd numbers from a series of numbers.

#Taking input from user as a list

size = int(input("Enter no of elements you want to enter : "))
numbers = []
for i in range(size):
    value = int(input(f"Enter {i+1} list elements : "))
    numbers.append(value)

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

