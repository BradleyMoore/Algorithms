def mergesort(unsorted):

    # if length of list is <= 1 it is already sorted
    if len(unsorted) <= 1:
        return unsorted

    mid = len(unsorted) / 2
    left = unsorted[:mid]
    right = unsorted[mid:]
    sorted = []
    print str(left) + ' <-- left'
    print str(right) + ' <-- right'

    # recursively split the lists down to lengths of 1
    if len(left) > 1:
        print str(left) + ' <-- merge left'
        left = mergesort(left)
    if len(right) > 1:
        print str(right) + ' <-- merge right'
        right = mergesort(right)

    i = 0
    j = 0
    iter_length = 0
    if len(left) > len(right):
        iter_length = len(right)
    else:
        iter_length = len(left)

    for k in xrange(len(unsorted)):
        # if one side gets finished just extend the rest of the other sorted side
        if i == len(left):
            sorted.extend(right[j:])
            j = j + 1
            print str(j) + ' <-- j'
            break
        elif j == len(right):
            sorted.extend(left[i:])
            i = i + 1
            print str(i) + ' <-- i'
            break

        # append lesser of the 2 options
        if left[i] < right[j]:
            sorted.append(left[i])
            i = i + 1
        else:
            sorted.append(right[j])
            j = j + 1

    print str(sorted) + ' <-- sorted'
    return sorted


if __name__ == '__main__':
    list = [4,7,3,2,57,4,345,768,89,345,234,56,768,789,768,4,23,45,568,89,0,6,234,2345,768,79,0,789,356,23,1,346,578,76,4,235,346,68,247,383,3,568,58,56,7,3,4,36,76,54]
    sort = mergesort(list)
    print str(sort) + ' <-- sort'

