''' 1.2 implement program to find a year is leap year or not using if else elif statement '''
year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year,"is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")