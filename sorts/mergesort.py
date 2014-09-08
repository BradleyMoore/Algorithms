def mergesort (unsorted):
	if len(unsorted <= 1):
		return unsorted
	
	mid = int(len(unsorted) / 2)
	left = unsorted[:mid]
	right = unsorted[mid:]
    sorted = [0 for i in xrange(unsorted)]

    if len(left) > 1:
        mergesort(left)
    else if len(right) > 1:
        mergesort(right)

    i = 0
    j = 0
    iter_length = 0
    if len(left) > len(right):
        iter_length = len(left)
    else:
        iter_length = len(right)

    

