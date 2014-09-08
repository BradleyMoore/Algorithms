'''
mergesort func
accept input
split
sort

split func
if len <= 1
	return input
else 
	mid = len unsorted / 2
	left = 0
	right = mid

sort func
while len left > 0 or len right > 0
	if len left < 1
		append right(all)
	else if len right < 1
		append left(all)
	else
		if left < right
			append left
		else append right
'''

def mergesort (unsorted):
	if len(unsorted <= 1):
		return unsorted
	
	mid = int(len(unsorted) / 2)
	left = unsorted[:mid]
	right = unsorted[mid:]
    sorted = []

    if len(left) > 1:
        mergesort(left)
    else if len(right) > 1:
        mergesort(right)

    i = 0
    j = 0

