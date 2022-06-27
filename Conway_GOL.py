import random,time,os
import numpy as np

os.system('clear')
x = 0
dim = 30
maindict = {}
locations = []
locations3 = []
live_cell = ' . '
dead_cell = '   '
boundary = [1,dim]

for num1 in range(dim):
    for num2 in range(dim):
        maindict[str(num1+1)+str(num2+1)] = dead_cell
        locations.append(str(num1+1)+str(num2+1))
        locations3.append(str(num1+1)+'|'+str(num2+1))
            
def printlist():
    for num1 in range(dim):
        for num2 in range(dim):
            print(maindict[str(num1+1)+str(num2+1)],end=' ')
            if (num2+1) == dim:
                print('\n')

def mainfunc(var,tr1):
    ccc1 = 0
    if (var not in boundary):
        for num in range(3):
            tempvar = var - 1 + num
            if maindict2[str(tr1)+str(tempvar)] == live_cell:
                ccc1 += 1
    else:
        for num in range(2):
            if (var == 1):
                tempvar = var + num
                if maindict2[str(tr1)+str(tempvar)] == live_cell:
                    ccc1 += 1
            elif (var == 5):
                tempvar = var - 1 + num
                if maindict2[str(tr1)+str(tempvar)] == live_cell:
                    ccc1 += 1
    return ccc1

def checkcell(x):
    r1 = int(locations2[x].split('|')[0])
    c1 = int(locations2[x].split('|')[1])
    ccc2 = 0

    if (r1 not in boundary):
        for num1 in range(3):
            tempr1 = r1 - 1 + num1
            ccc2 += mainfunc(c1,tempr1)
    else:
        for num1 in range(2):
            if (r1 == 1):
                tempr1 = r1 + num1
                ccc2 += mainfunc(c1,tempr1)
            elif (r1 == 5):
                tempr1 = r1 - 1 + num1
                ccc2 += mainfunc(c1,tempr1)
    if maindict2[str(r1)+str(c1)] == live_cell:
        ccc2 = ccc2 - 1
    return ccc2


seedcells = []
initialpop = int(0.5*(dim**2))
for num in range(initialpop):
    seedcells.append(random.choice(locations))

for num in range(initialpop):
    maindict[seedcells[num]] = live_cell

print("Starting population!")
printlist()
time.sleep(3)

while live_cell in maindict.values():
    os.system('clear')
    locations2 = locations3.copy()
    maindict2 = maindict.copy()
    for num in range(len(locations)):
        tempvalue = checkcell(num)
        if (tempvalue < 2) or (tempvalue > 3):
            maindict[locations[num]] = dead_cell
        elif tempvalue == 3:
            maindict[locations[num]] = live_cell

    x += 1
    print(f"Cycle: {x} | Live: {list(maindict.values()).count(live_cell)}")
    printlist()
    time.sleep(0.15)

if live_cell not in maindict.values():
    print("All dead! O_O ")