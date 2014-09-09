import sys


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
        left = mergesort(left)
    if len(right) > 1:
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
            break
        elif j == len(right):
            sorted.extend(left[i:])
            i = i + 1
            break

        # append lesser of the 2 options
        if left[i] < right[j]:
            sorted.append(left[i])
            i = i + 1
        else:
            sorted.append(right[j])
            j = j + 1

    return sorted


if __name__ == '__main__':
    unsorted = [3,345,456,7,879,970,7,4,23,123,45,467,578,78,6,4,324,145,345,3456,567,5768,6589,69,69]
    sort = mergesort(unsorted)
    print '%r <-- unsorted' % unsorted
    print '%r <-- sorted' % sort

