def quicksort(array):
    if(len(array) == 0):
        return array
    pivot = array[-1]
    pivot_index = -1
    i = -1
    for j in range(len(array)):
        if(array[j] < pivot):
            i+=1
            array = swap(array, i, j)
        if(j == len(array)-1):
            pivot_index = i+1
            swap(array, j, pivot_index)
    if(len(array) == 1):
        return array

    left_sorted_array = quicksort(array[:pivot_index])
    right_sorted_array = quicksort(array[pivot_index+1:])

    if(len(right_sorted_array) > 1):
        k = 0
        while(pivot_index < len(array) and k < len(right_sorted_array)):
            array[pivot_index + 1] = right_sorted_array[k]
            k+=1
            pivot_index += 1

    if(len(left_sorted_array) > 1):
        k = 0
        pivot_index = 0
        while(pivot_index < len(array) and k < len(left_sorted_array)):
            array[pivot_index] = left_sorted_array[k]
            k+=1
            pivot_index +=1
    return array

def swap(array, i, j):
    number = array[j]
    array[j] = array[i]
    array[i] = number
    return array

array = [10, 20, 60, 90, 80, 90, 30, 70]
print(quicksort(array))
