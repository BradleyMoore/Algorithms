def mergesort(unsorted):

    # if length of list is <= 1 it is already sorted
    if len(unsorted) <= 1:
        return unsorted

    mid = len(unsorted) / 2
    left = unsorted[:mid]
    right = unsorted[mid:]
    sorted = []

    # recursively split the lists down to lengths of 1
    if len(left) > 1:
        mergesort(left)
    elif len(right) > 1:
        mergesort(right)

    i = 0
    j = 0
    iter_length = 0
    if len(left) > len(right):
        iter_length = len(right)
    else:
        iter_length = len(left)

    for k in xrange(iter_length):
        # if one side gets finished just append the rest of the other sorted side
        if i == len(left):
            sorted.append(right[j:])
        elif j == len(right):
            sorted.append(left[i:])

        # append lesser of the 2 options
        if left[i] < right[j]:
            sorted.append(left[i])
            i = i + 1
        else:
            sorted.append(right[j])
            j = j + 1

    print sorted


while __name__ == '__main__':
    list = [1,245,356,467,689,678,3456,234,234,234,346,56,231,212,13,24,345,456,68,76,345,34,134]
    mergesort(list)

