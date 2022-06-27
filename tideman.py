import os
import numpy as np

os.system('clear')

dict = {}
candidates = []
can_count = int(input("How many candidates do you want? "))
for num in range(can_count):
    tmpvalue = input(f"Please enter Candidate{num+1} name: ")
    candidates.append(tmpvalue)
    key = str("rank"+str(num+1))
    dict[key] = 0

scores = np.eye(len(candidates))
fin_score = [np.zeros(len(candidates))]

voter_count = '-'
while not isinstance(voter_count,int):
    voter_count = input("No. of voters: ")
    if voter_count.isnumeric():
        voter_count = int(voter_count)

def convertlist(listhere):
    for num in range(len(candidates)):
        tmplist[num] = listhere[num] > 0

###########################################################

for num in range(voter_count):
    print(f"Round {num+1}: ")
    tmprank = []
    for num in range(len(candidates)):
        tmprank.append('-')
    
    dict['rank1'] = input("Rank 1: ")
    tmprank[0] = dict['rank1']
    while True:
        dict['rank2'] = input("Rank 2: ")
        if (dict['rank2'] in tmprank) or (dict['rank2'] not in candidates):
            print("Please enter a different name.")
            continue
        tmprank[1] = dict['rank2']
        break
    while True:
        dict['rank3'] = input("Rank 3: ")
        if (dict['rank3'] in tmprank) or (dict['rank3'] not in candidates):
            print("Please enter a different name.")
            continue
        tmprank[2] = dict['rank3']
        break
    print('---------')

    for num1 in range(len(candidates)):
        for num2 in range(num1,len(candidates)):
                scores[candidates.index(dict['rank'+str(num1+1)])][candidates.index(dict['rank'+str(num2+1)])] += 1

for num in range(len(candidates)):
    if (num+1) != len(candidates):
        fin_score[num] = scores[num][num+1] - scores[num+1][num]
    elif (num+1) == len(candidates):
        fin_score[num] = scores[num][0] - scores[0][num]

tmplist = np.zeros(len(candidates))
tmplist2 = np.zeros(len(candidates))
convertlist(fin_score)

fin_score_copy = fin_score.copy()
if (np.count_nonzero(tmplist == True) > 1):
    if fin_score_copy.index(max(fin_score_copy)) == 0:
        tmplist2[0] += 1
        tmplist2[1] -= 1
        fin_score_copy[0] = min(fin_score)
    if fin_score_copy.index(max(fin_score_copy)) == 1:
        tmplist2[1] += 1
        tmplist2[2] -= 1
        fin_score_copy[1] = min(fin_score)
    if fin_score_copy.index(max(fin_score_copy)) == 2:
        tmplist2[2] += 1
        tmplist2[0] -= 1
        fin_score_copy[2] = min(fin_score)
    convertlist(tmplist2)

try:    
    print("Winner: " + candidates[tmplist.index(True)].capitalize() + "! ")
    print(fin_score)
    print(scores)
except:
    if (np.count_nonzero(tmplist == True) == 0):
        print("Tough match! Its a tie!")
        print(fin_score)
        print(tmplist)

print(fin_score)
print(tmplist)
print(scores)