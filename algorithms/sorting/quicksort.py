from random import randint


def quicksort(unsorted, start=0, end=0):
    if len(unsorted) <= 1:
        return unsorted

    sorted = sort(unsorted, start, end)

    return sorted


def choose_pivot(start, end):
    pivot = randint(start, end-1)

    return pivot


def sort(unsorted, pivot, start=0, end=0):
    if end == 0:
        end = len(unsorted)

    pivot = choose_pivot(start, end)

    last_less = 0
    for i in xrange(start, end):
        if unsorted[i] < unsorted[pivot]:
            unsorted.insert(last_less, unsorted[i])
            unsorted.remove(unsorted[i])
            if i > pivot:
                pivot = pivot + 1
            last_less = last_less + 1
            continue
        elif unsorted[i] > unsorted[pivot]:
            unsorted.insert(end, unsorted[i])
            unsorted.remove(unsorted[i])
            if i < pivot:
                pivot = pivot - 1
            continue
        else:
            continue

    unsorted[i], unsorted[pivot] = unsorted[pivot], unsorted[i]

    partial_sort = quicksort(unsorted, 0, pivot-1)
    partial_sort = quicksort(partial_sort, pivot+1, len(unsorted))

    sorted = partial_sort
    return sorted


if __name__ == '__main__':
    unsorted = [3,345,456,7,879,970,7,4,23,123,45,467,578,78,6,4,324,145,345,3456,567,5768,6589,69,69]
    sort = quicksort(unsorted)

    print '%r <-- unsorted' % unsorted
    print '%r <-- sorted' % sort
