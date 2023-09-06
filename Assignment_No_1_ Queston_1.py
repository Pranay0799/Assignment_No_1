# Write a Python program to get the Fibonacci series between 0 to 50

num_1 = int(input("Enter the First Number of Fibonacci series : "))
num_2 = int(input("Enter the Second Number of Fibonacci series : "))  
l_num = int(input("Enter the Max Number of Fibonacci series but not more than 50: "))

while num_2 <= l_num:
    print(num_2, end="  ")
    num_1, num_2 = num_2, num_1 + num_2

    
#### Thank You.... 
