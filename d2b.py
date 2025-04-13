class usermaincode():
    @classmethod
    def d2b(cls,num):
        st = ""
        while num > 0:
            r = num % 2
            st = st + str(r)
            num = num // 2
            
        return int(st[::-1])
n = 37
a = usermaincode()
print(a.d2b(n))

