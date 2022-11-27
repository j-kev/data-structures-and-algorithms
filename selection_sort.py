def selection_sort(array):
    for i in range(len(array) - 1):
        lowest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest]:
                lowest = j
        if lowest != i:
            array[i], array[lowest] = array[lowest], array[i]
    return array


if __name__ == '__main__':
    a = [9, 3, 6, 8, 5, 2, 0, 1, 7, 4]
    assert selection_sort(a) == [x for x in range(10)]
