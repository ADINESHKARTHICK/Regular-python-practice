num = int(input('Enter the number: '))
original = num
temp = num

count = 0

while temp > 0:
    x = temp % 10
    temp = temp // 10
    count += 1

sum = 0

while num > 0:
    val = num % 10
    num = num // 10

    power = 1

    for i in range(count):
        power = power * val

    sum = sum + power

if sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")
        

    
