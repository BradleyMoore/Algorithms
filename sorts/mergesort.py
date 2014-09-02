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
	if len(unsorted > 1):
		split(unsorted)
	else:
		return unsorted


def split(unsorted):
	mid = int(len(unsorted) / 2)
	left = unsorted[:mid]
	right = unsorted[mid:]

	if len(left) > 1:
		mergesort(left)
	if len(right) > 1:
		mergesort(right)

	sort(unsorted)

def sort(unsorted):
	
















	







