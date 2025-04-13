class usermaincode():
    @classmethod
    def pallindrome(cls,str):
        if str == str[::-1]:
            return "given string is a pallindrome"
        else:
            return "given string is NOT a pallindrome"
str = "abccba"
a = usermaincode()
print(a.pallindrome(str))