def task(array=input("Введите массив чисел: ")):
    array = list(str(array))
    length = len(array)
    left = -1
    right = length
    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] == '0':
            right = middle
        else:
            left = middle
    return right
