class usermaincode():
    @classmethod
    def reverse(cls,n):
        rev = 0
        while n > 0:
            rev = rev*10 + (n % 10)
            n = n//10
        return rev
    
n = 986547
a =usermaincode()
print(a.reverse(n))
