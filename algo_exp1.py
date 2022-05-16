def firstNonRepeating(arr, n):
    new_arr = []
    for ar in range(len(arr)):
        j = 0
        while (j < len(arr)):
            if (ar != j and arr[ar] == arr[j]):
                break
            j += 1
        if j == n:
            return arr[ar]
    return -1
      
# Driver code
arr = [7, 9, 4, 6, 7, 4 ]
n = len(arr)
print(firstNonRepeating(arr, n))