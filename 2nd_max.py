def sec_max(arr):
    first_max = max(arr[0],arr[1])
    second_max = min(arr[0],arr[1])
    n = len(arr)
    for i in range (2,n):
        if arr[i]>first_max:
            second_max = first_max
            first_max = arr[i]
        elif arr[i] > second_max:
            second_max = arr[i]
    return second_max

arr =[55,1,45,68,159,75,5,14]
print(sec_max(arr))