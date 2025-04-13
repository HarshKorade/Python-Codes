class usermaincode():
    @classmethod
    def snx(cls,input1,input2):
        s = 0 
        x = 0
        for i in range(input1):
            if i % 2 == 0:
                x = x^input2[i]
            else:
                s += input2[i]
        return s-x
input1 = 6
input2 = [10,5,6,3,7,2]
a = usermaincode()
print(a.snx(input1,input2))
