year = int(input("Enter a number :"))

if(year % 4) == 0:
	print("{0} is a leap year". format(year))
else:
	print("{0} is not a leap year". format(year))