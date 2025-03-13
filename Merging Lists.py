def merge_and_remove_duplicates(list1, list2):
  merged_list = list1 + list2
  unique_elements = []
  for element in merged_list:
    if element not in unique_elements:
      unique_elements.append(element)
  return unique_elements