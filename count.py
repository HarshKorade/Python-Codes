class USERMAINCODE():
    @classmethod
    def count(cls,input1,input2,input3):
        ans = 0
        for i in range(input2):
            if input1[i] == input3:
                ans += 1
        return ans 
input1 = "whatisthat"
input2 = len(input1)
input3 = "a"
a = USERMAINCODE()
print(a.count(input1,input2,input3))
