def binary_search(sorted_array, target):
    lower = 0 
    upper = len(sorted_array) - 1

    while lower <= upper:
        midpoint = (lower + upper) // 2
        value = sorted_array[midpoint]

        if value == target:
            return midpoint
        elif value < target:
            lower = midpoint + 1
        else:
            upper = midpoint - 1
    return None



assert binary_search([0, 2, 4, 6, 8], 0) == 0
assert binary_search([1, 3, 5, 7, 9], 3) == 1
assert binary_search([-9, 2, 13, 27, 31], 13) == 2
assert binary_search([-9, 2, 13, 27, 31], 27) == 3
