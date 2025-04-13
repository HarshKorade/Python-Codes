class USERMAINCODE():
    @classmethod
    def rebound(cls,input1,input2,input3):
        e = input2/input3
        e_new = e**2
        h = input1 * e_new
        return h
input1 = 10
input2 = 20
input3 = 5
a = USERMAINCODE()
print(a.rebound(input1,input2,input3))