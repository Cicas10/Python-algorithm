def bubbleSort(array):
    flag = True
    n = array.__len__() - 2
    while flag:
        flag = False
        for i in range(n):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                flag = True
        n -= 1
    return array

# MAIN

inputString = input("Insert some numbers to be ordered: (ex. 3,1,2)")
arrayString = inputString.split(',')
arrayInt = list(map(int, arrayString))
print(bubbleSort(arrayInt))


