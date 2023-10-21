### Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?


def find_pairs(lst, num):
    pairList = []
    s_pair = set()
    seen = set()

    for i in lst:
        check = num - i
        if check in seen:
            pair = (min(i, check), max(i, check))
            if pair not in s_pair:
                pairList.append(pair)
                s_pair.add(pair)
        seen.add(i)

    return pairList

size = int(input("Enter the number of elements in the list: "))
list_num = []

for i in range(size):
    ele = int(input(f"Enter element {i+1}: "))
    list_num.append(ele)

num = int(input("Enter the target sum: "))

result = find_pairs(list_num, num)
print(result)































