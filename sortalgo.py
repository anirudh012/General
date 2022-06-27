import time, os
from random import shuffle

os.system('clear')
mylist = list(range(0,10000))
shuffle(mylist)

###########################

lin_sort = mylist.copy()
newlist = []

start1 = time.time()
for num in range(0,len(lin_sort)):
    newlist.append(min(lin_sort))
    lin_sort.remove(min(lin_sort))
    
end1 = time.time()
final1 = end1 - start1

###########################

bubble_sort = mylist.copy()

i = 0

start2 = time.time()
while True:
    if bubble_sort[i] > bubble_sort[i+1]:
        a = bubble_sort[i]
        b = bubble_sort[i+1]
        bubble_sort[i] = b
        bubble_sort[i+1] = a
    i += 1
    if ((i+1) == len(bubble_sort)):
        i = 0
    check = 0
    for num in range(0,len(bubble_sort)-1):
        if bubble_sort[num] > bubble_sort[num+1]:
            check = 0
            break
        elif bubble_sort[num] <= bubble_sort[num+1]:
            check += 1
    if check == (len(bubble_sort)-1):
        break

end2 = time.time()
final2 = end2 - start2

###########################

merge_sort = mylist.copy()

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2

		L = arr[:mid]
		R = arr[mid:]

		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

start3 = time.time()
mergeSort(merge_sort)
end3 = time.time()
final3 = end3 - start3

###########################

print(final1)
print(final2)
print(final3)