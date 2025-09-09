number1=int(input("enter the 1st number"))
number2=int(input("enter the 2st number"))
number3=int(input("enter the 3st number"))
if number1 > number2 and number1 > number3:
    print(f'{number1} is a gretest number')
elif number2 > number3 and number2 >number1:
    print(f'{number2} is a gretest number')
else:
    print(f'{number3} is a gretest number')
