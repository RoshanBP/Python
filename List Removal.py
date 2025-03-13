my_list = [1, 2, 3, 4, 5]

# Remove element using remove()
print("Original list:", my_list)
my_list.remove(3)
print("List after removing 3:", my_list)

# Remove element using pop()
print("Original list:", my_list)
removed_element = my_list.pop(1)
print("Removed element:", removed_element)
print("List after popping element at index 1:", my_list)