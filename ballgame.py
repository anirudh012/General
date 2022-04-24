import random
from random import shuffle

mylist = [1,0,0]
randlist = [0,2]
playmode = "Y"
scorecard = 0
totalplay = 0

simcheck = 0
ogcheck = 0
simulation1 = int(input("How many tests? "))

g0 = 0
g1 = 0
g2 = 0

a0 = 0
a1 = 0
a2 = 0

w0 = 0
w1 = 0
w2 = 0

while simcheck < simulation1:

	shuffle(mylist)
	minlist = [a0,a1,a2]

	if ogcheck%10 == 0:
		ogcheck = 0
	else:
		ogcheck += 1

	if ogcheck < 5:
		finalguess = int(random.randint(0,2))
	else:
		finalguess = minlist.index(max(minlist))

	if finalguess == 0:
		g0 += 1
	elif finalguess == 1:
		g1 += 1
	else:
		g2 += 1
		
	if finalguess == mylist.index(1):
		print("My guess is: " + str(finalguess))
		print("Correct! You won.")
		print(mylist)
		scorecard = scorecard + 1
		totalplay = totalplay + 1
		simcheck += 1
		print("Current score " + str(scorecard) + ". Total play " + str(totalplay) + ". Accuracy rate " + str(scorecard/totalplay))
		if finalguess == 0:
			w0 += 1
			a0 = w0/g0
		elif finalguess == 1:
			w1 += 1
			a1 = w1/g1
		else:
			w2 += 1
			a2 = w2/g2

		print("FG " + str(a0))
		print("FG " + str(a1))
		print("FG " + str(a2))
		print('\n')
		print('---------------------')
		print('\n')	

	else:
		print("My guess is: " + str(finalguess))
		print("Wrong answer!")
		print(mylist)
		scorecard = scorecard + 0
		totalplay = totalplay + 1
		simcheck += 1
		print("Current score " + str(scorecard) + ". Total play " + str(totalplay) + ". Accuracy rate " + str(scorecard/totalplay))
		if finalguess == 0:
			w0 += 0
			a0 = w0/g0
		elif finalguess == 1:
			w1 += 0
			a1 = w1/g1
		else:
			w2 += 0
			a2 = w2/g2

		print("FG " + str(a0))
		print("FG " + str(a1))
		print("FG " + str(a2))

		print('\n')
		print('---------------------')
		print('\n')	
