x = str(input("Please input your credit card number. "))

mynum = []

for num in x:
    num = int(num)
    mynum.append(num)

mynum.reverse()

sum_holder = 0
for num in mynum:
    num = int(num)
    if mynum.index(num) % 2 == 1:
        num2 = num * 2
        sum_holder = sum_holder + (num2//10) + (num2%10)
    else:
        sum_holder = sum_holder + (num//10) + (num%10)
    mynum[mynum.index(num)] = 'a'

sum_holder = str(sum_holder)
if sum_holder[len(sum_holder)-1] == '0':
    print("Valid")
else:
    print("Invalid")
