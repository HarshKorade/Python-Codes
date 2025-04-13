class ans():
    @classmethod
    def reverse(cls,input1,input2):
        input1 = list(input1)
        x = input1[::-1]
        return sum(x[i] for i in range(input2) if i % 2 == 0)
input1 = [10,20,30,40,50,60]
input2 = 6
a = ans()
print(a.reverse(input1,input2))