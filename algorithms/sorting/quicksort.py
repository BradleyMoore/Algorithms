import random


def quicksort(unsorted):
    """Input unsorted list and return either list if len < 2 or return sorted list"""
    if len(unsorted)<2:
        return unsorted

    pivot = choose_pivot(unsorted)
    left, equals, right = partition(unsorted, pivot)

    sorted = quicksort(left) + equals + quicksort(right)
    return sorted


def choose_pivot(unsorted):
    """Input unsorted list and return a random item from it"""
    pivot = random.choice(unsorted)
    return pivot


def partition(unsorted, pivot):
    """Input unsorted list and the randomized element and return 3 quicksorted lists"""
    left = [i for i in unsorted if i < pivot]
    equals = [i for i in unsorted if i == pivot]
    right = [i for i in unsorted if i > pivot]

    return left, equals, right


if __name__ == '__main__':
    unsorted = [3,345,456,7,879,970,7,4,23,123,45,467,578,78,6,4,324,145,345,3456,567,5768,6589,69,69]
    sorted = quicksort(unsorted)

    print '%r <-- unsorted' % unsorted
    print '%r <-- sorted' % sorted

