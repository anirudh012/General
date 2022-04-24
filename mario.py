
x = int(input("Height of pyramid needed. ")) + 1

for num in range(x):
    print((" "*(x - num) + "#"*num + " ") + ("#"*num))
