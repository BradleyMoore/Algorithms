def mergesort (unsorted):
    # if length of lilst is <= 1 it is already sorted
	if len(unsorted <= 1):
		return unsorted
	
	mid = int(len(unsorted) / 2)
	left = unsorted[:mid]
	right = unsorted[mid:]
    sorted = []

    # recursively split the lists down to lengths of 1
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
    
    for k in xrange(unsorted):
        # if one side gets finished just append the rest of the other sorted side
        if i == len(left):
           sorted.append(right[j:]
        else if j == len(right):
            sorted.append(left[i:]




