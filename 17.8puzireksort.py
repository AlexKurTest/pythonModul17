array = [2, 3, 1, 4, 6, 5, 9, 8, 7, 10, 13, 11, 12, 15, 14]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)