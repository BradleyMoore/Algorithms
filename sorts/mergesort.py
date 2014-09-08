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

