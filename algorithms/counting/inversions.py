from ..sorting.mergesort import mergesort


def inversions(unsorted1, unsorted2):
    invs = 0
    sorted1 = []
    sorted2 = []

    # merge sort at n*log(n); it's essentially free in this case
    sorted1 = mergesort(unsorted1)
    sorted2 = mergesort(unsorted2)

    invs = find_inversions(sorted1, sorted2)

    return (sorted1, sorted2, invs)


def find_inversions(sorted1, sorted2):
    '''
    essentially rewrite merge function from sorting.mergesort
    to add in counting inversions and to avoid adding
    unessissary bloat to mergesort module
    '''
    i = 0
    j = 0
    invs = 0
    for k in xrange(len(sorted1) + len(sorted2)):
        if i == len(sorted1):
            break
        elif j == len(sorted2):
            break

        if sorted1[i] < sorted2[j] or sorted1[i] == sorted2[j]:
            i = i + 1
        else:
            invs = invs + 1
            j = j + 1

    return invs
    

if __name__ == '__main__':
    list1 = [1,3,5,2345,76,7689,5,345,123,56,45,645,234,23,345]
    list2 = [2,4,5,56,578,768,234,123,123,234,345,56,76,5,2343]
    sorted1 = []
    sorted2 = []

    sorted1, sorted2, invs = inversions(list1, list2)

    print sorted1
    print sorted2
    print '%d <-- inversions' % invs

