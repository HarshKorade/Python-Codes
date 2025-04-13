class usermaincode():
    @classmethod
    def leap(cls,year):
        if (year % 400 == 0 and year % 100 == 0):
            return f"{year} is a leap year"
        elif (year % 4 == 0 and year % 100 != 0):
            return f"{year} is a leap year"
        else:
            return f"{year} is NOT a leap year"

year = 2025
a = usermaincode()
print(a.leap(year))