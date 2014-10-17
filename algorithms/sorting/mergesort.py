import sys


def mergesort(unsorted):
    """Takes an unsorted list as imput and return a sorted list."""
    sorted = []

    # if length of list is <= 1 it is already sorted
    if len(unsorted) <= 1:
        return unsorted

    # split list into 2 halves
    left, right = split_list(unsorted)

    # sort and merge the 2 list halves
    sorted = merge(left, right)

    return sorted


def split_list(unsorted):
    """Takes an unsorted list as input and returns 2 lenght n/2 unstored lists in a tuple."""
    mid = len(unsorted) / 2
    left = unsorted[:mid]
    right = unsorted[mid:]

    # recursively split the lists down to lengths of 1
    if len(left) > 1:
        left = mergesort(left)
    if len(right) > 1:
        right = mergesort(right)

    return (left, right)


def merge(left, right):
    """Takes 2 unsorted lists and returns 1 sorted list."""
    sorted = []

    i = 0
    j = 0
    for k in xrange(len(left) + len(right)):
        # if one side gets finished just extend the rest of the other sorted side
        if i == len(left):
            sorted.extend(right[j:])
            break
        elif j == len(right):
            sorted.extend(left[i:])
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
