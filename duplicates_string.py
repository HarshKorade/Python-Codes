class solution:
    def remove_duplicate(self,str):
        s =""
        for i in str:
            if i not in s:
                s = s+i
        return s    
a = solution()
str = "GEeKsforgeEKs"
print(a.remove_duplicate(str))