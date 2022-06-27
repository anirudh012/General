import os

os.system('clear')

n = int(input("How many numbers?: "))

def fibonnaci_rec(n):
    
    if n <= 2:
        return 1
    else:
        return fibonnaci_rec(n-1) + fibonnaci_rec(n-2)

print(fibonnaci_rec(n))