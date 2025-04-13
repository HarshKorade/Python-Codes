class usermsincode():
    @classmethod
    def hcf(cls,num1,num2):
        if num1 > num2:
            x = num2
        else:
            x = num1
        for i in range(1,x+1):
            if num1 % i == 0 and num2 % i == 0:
                hcf = i
        return hcf
n = 36
n1 = 42
a = usermsincode()
print(a.hcf(n,n1))