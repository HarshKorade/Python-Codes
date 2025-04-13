class solution:
    def pushZeroes(self,arr,n):
        l = 0
        for r in range(n):
            if arr[r] != 0:
                arr[l],arr[r] = arr[r],arr[l]
                l += 1
        return arr
    
arr = [3,5,0,0,4]
n = 5
a = solution()
print(a.pushZeroes(arr,n))