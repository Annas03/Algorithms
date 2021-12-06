import math

def mergesort(arr):
    l = 0
    r = len(arr) - 1
    if(len(arr) > 2):
        m = l +(r - 1)/2
        m = math.ceil(m)
        leftarray = arr[:m+1]
        rightarray = arr[m+1:]

        sorted_left_array = mergesort(leftarray)
        sorted_right_array = mergesort(rightarray)
        
        sorted_array = []

        i = 0
        j = 0
        while(i < len(sorted_left_array)):
            while(j < len(sorted_right_array)):
                if(sorted_left_array[i] == sorted_right_array[j]):
                    sorted_array.append(sorted_left_array[i])
                elif(sorted_left_array[i] < sorted_right_array[j]):
                    sorted_array.append(sorted_left_array[i])
                    if(i == len(sorted_left_array)-1):
                        while(j < len(sorted_right_array)):
                            sorted_array.append(sorted_right_array[j])
                            j+=1
                    break
                elif(sorted_left_array[i] > sorted_right_array[j]):
                    sorted_array.append(sorted_right_array[j])
                    if(len(sorted_right_array) == 1):
                        while(i < len(sorted_left_array)):
                            sorted_array.append(sorted_left_array[i])
                            i+=1
                    if(j == len(sorted_left_array)-1):
                        while(i < len(sorted_left_array)):
                            sorted_array.append(sorted_left_array[i])
                            i+=1
                j+=1
            i+=1               
        return sorted_array
                    
    elif(len(arr) == 2):
        leftarray = arr[l]
        rightarray = arr[r]
        if(leftarray > rightarray):
            arr[l] = rightarray
            arr[r] = leftarray
        return arr
    else:
        return arr
		
a = [1, 99099, 9999, 10000]
print(mergesort(a))
    


