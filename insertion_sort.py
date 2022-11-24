def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        position = i - 1

        while position >= 0:
            if array[position] > temp:
                array[position + 1] = array[position]
                position -= 1
            else:
                break

        array[position + 1] = temp

    return array
        

a = [5, 3, 4, 2, 0, 1]
assert insertion_sort(a) == [0, 1, 2, 3, 4, 5]
