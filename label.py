class usermaincode():
    @classmethod
    def label(cls,input1,input2):
        ans = ""
        for i in input1:
            if i % 2 == 0:
                ans += " Even"
            else:
                ans += " Odd"
        return ans 
input1 = [1,2,3,4,5,6]
input2 = 6
a = usermaincode()
print(a.label(input1,input2))