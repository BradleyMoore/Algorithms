from random import randint


def partition(unsorted, start, end, pivot):
    pass


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
