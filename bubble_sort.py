def bubble_sort(array):
    length = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        length -= 1

    return array


if __name__ == '__main__':
    assert bubble_sort([5, 4, 3, 2, 0, 1]) == [0, 1, 2, 3, 4, 5]
