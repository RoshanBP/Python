def find_largest_smallest(numbers):
    if not numbers:
        return None, None
    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    return largest, smallest