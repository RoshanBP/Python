def count_element(lst, element):
  count = 0
  for item in lst:
    if item == element:
      count += 1
  return count

# Example usage
my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_count = 2
count = count_element(my_list, element_to_count)
print(f"The element '{element_to_count}' appears {count} times in the list.")