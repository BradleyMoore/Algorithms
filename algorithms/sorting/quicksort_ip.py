from random import randint


def partition(unsorted, start, end, pivot):
    """Return final resting place of pivot; RIP sweet pivot."""
    pivot = unsorted[choose_pivot(start, end)]

    # move pivot to beginning for logic
    unsorted[start], unsorted[pivot] = unsorted[pivot], unsorted[start]
    i = start + 1
    j = start + 1

    # move elements less than pivot to the left so the pivot can be swapped later
    while j < end:
        if unsorted[j] < pivot:
            unsorted[j], unsorted[i] = unsorted[i], unsorted[j]
            i = i + 1
        j = j + 1

    unsorted[start], unsorted[pivot] = unsorted[pivot], unsorted[start]
    return i - 1


def choose_pivot(start, end):
    """Input start and end locations of list and return a random number between the 2."""
    pivot = randint(start, end)
    return pivot


def quicksort(unsorted, start=0, end=None):
    pass


if __name__ == '__main__':
    unsorted = [3,345,456,7,879,970,7,4,23,123,45,467,578,78,6,4,324,145,345,3456,567,5768,6589,69,69]
    sorted = quicksort(unsorted)

    print '%r <-- unsorted' % unsorted
    print '%r <-- sorted' % sorted
