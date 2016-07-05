# quick sort algorithm
def quickSort(list, start, end):
    if start < end:
        # partition the list
        split = partition(list, start, end)
        # sort both halves
        quickSort(list, start, split-1)
        quickSort(list, split+1, end)
    return list

def partition(list, start, end):
    pivot = list[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and list[left] <= pivot:
            left += 1
        while list[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            # swap numbers
            temp = list[left]
            list[left] = list[right]
            list[right] = temp
    # swap start with list[right]
    temp = list[start]
    list[start] = list[right]
    list[right] = temp
    return right


inputString = input("Insert some numbers to be ordered: (ex. 3,1,2)")
arrayString = inputString.split(',')
arrayInt = list(map(int, arrayString))
print(quickSort(arrayInt, 0, len(arrayInt)-1))
