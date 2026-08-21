operator=input('Enter the operator + - * / :')
num1=int(input('Enter the num1'))
num2=int(input('Enter the num2'))
if(operator=='+'):
    res=num1+num2
elif(operator=='-'):
    res=num1-num2
elif(operator=='*'):
    res=num1*num2
elif(operator=='/'):
    res=num1/num2
else:
    print('Invalid Operator , Enter the correct operator')
print(f'The result is:{res}')
