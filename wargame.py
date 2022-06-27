import os, time
from random import shuffle

def wargame():

    my_dict = {}
    suits = ['Hearts','Clubs','Diamonds','Spades']
    ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
    fulldeck = []

    for suit in suits:
        for rank in ranks:
            fulldeck.append(rank + ' of ' + suit)

    for key in fulldeck:
        if len(my_dict) % 13 == 0:
                num_ranks = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        for value in num_ranks:
            my_dict[key] = value
            num_ranks.remove(value)
            break

    shuffle(fulldeck)

    def dividelist(l):
        for i in range(0,len(l),int(len(l)/2)):
            yield l[i:i+int(len(l)/2)]
    
    x = list(dividelist(fulldeck))

    p1_list = x[0]
    p2_list = x[1]

    while ((len(p1_list))> 0) and ((len(p2_list))> 0):

        i = 0

        if my_dict[p1_list[i]] > my_dict[p2_list[i]]:
            p1_list.append(p1_list[i])
            p1_list.pop(i)
            p1_list.append(p2_list[i])
            p2_list.pop(i)
        elif my_dict[p1_list[i]] < my_dict[p2_list[i]]:
            p2_list.append(p2_list[i])
            p2_list.pop(i)
            p2_list.append(p1_list[i])
            p1_list.pop(i)

        while (((len(p1_list) - i) > 0) and ((len(p2_list) - i) > 0) and (my_dict[p1_list[i]] == my_dict[p2_list[i]])):

            i = i + 1
            
            if my_dict[p1_list[i]] > my_dict[p2_list[i]]:
                for num in range(i+1):
                    p1_list.append(p1_list[0])
                    p1_list.pop(0)
                    p1_list.append(p2_list[0])
                    p2_list.pop(0)
                break
            elif my_dict[p1_list[i]] < my_dict[p2_list[i]]:
                for num in range(i+1):
                    p2_list.append(p2_list[0])
                    p2_list.pop(0)
                    p2_list.append(p1_list[0])
                    p1_list.pop(0)
                break

    if (len(p2_list)) == 0:
        print("Player 1 won!")
    elif (len(p1_list)) == 0:
        print("Player 2 won!")

wargame()