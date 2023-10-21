### Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.


size = int(input("Enter no of ele  in list :"))
list_num = []
for i in range(size):
    ele = int(input(f"Enter the {i+1} element : "))
    list_num.append(ele)
print(list_num)

def rev_list(list_num):
    list_num = list_num[::-1]
    return list_num