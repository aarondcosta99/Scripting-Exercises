#!/c/Program Files/Python312/python
num = input('Enter a number please ')
number = int(num)
if number > 0:
    print(f'{number} is a positive number.')
elif number < 0:
    print(f'{number} is a negative number.')
else:
    print(f'{number} is zero.')