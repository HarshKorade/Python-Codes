class usermaincode():
    @classmethod
    def armstrong(cls,num):
        sum = 0
        n = num
        x = len(str(num))
        while n > 0:
            rem = n % 10
            sum = sum + (rem**x)
            n = n // 10
        if sum == num:
            return "yes"
        else:
            return "no"
n = 153
a = usermaincode()
print(a.armstrong(n)) 
        
