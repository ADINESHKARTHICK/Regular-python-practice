import random
num1=random.randint(1,10)
num2=random.randint(1,10)
product=num1*num2
generate_num=int(input())
if product==generate_num:
    print('Your answer is correct')
else:
    print('Your answer is wrong')
    print('The product value is: ',product)
