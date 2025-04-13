class usermaincode():
    @classmethod
    
    def nprime(cls,n):
            prime = True
            for i in range(2,n):
                for j in range(2,i):
                     if i %j == 0:
                       prime = False
                       break
                     else:
                        prime = True
                if prime == True:
                    print (i , end =" ")
            

n = 78
a = usermaincode()
print(a.nprime(n))