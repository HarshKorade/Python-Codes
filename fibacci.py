class usermaincode():
    @classmethod
    def fibonacci(cls, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        f = 0
        s = 1
        for i in range(3, n + 1):
            new = f + s
            f = s
            s = new
        return new
