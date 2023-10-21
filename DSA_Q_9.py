### Q9. Write a program to reverse a stack.


def reverse_stack(stack):
    reversed_stack = []

    while stack:
        item = stack.pop()
        reversed_stack.append(item)

    return reversed_stack


size = int(input("Enter the number of elements in the list: "))
stack = []
for i in range(size):
    ele = int(input(f"Enter element {i+1}: "))
    stack.append(ele)


print("Original Stack:", stack)
reversed_stack = reverse_stack(stack)
print("Reversed Stack:", reversed_stack)
