def linear_search(array, target):
    for item in range(len(array)):
        if target == array[item]:
            return item
    return -1


if __name__ == '__main__':
    assert linear_search([2, 3, 5, 6], 2) == 0
    assert linear_search([1, -5, 5, 7], -5) == 1
    assert linear_search([2, 1, 4, 9], 4) == 2
    assert linear_search([9, -7, -1, 0], 0) == 3
