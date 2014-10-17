from random import randint

def quicksort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
        
    start = 0
    end = start + 1
    pivot = choose_pivot(start, end)
    
    sort(unsorted, start, pivot, end)
    
    

def choose_pivot(start, end):
    pivot = randint(start, end)
    
    return pivot


def sort(unsorted, start, pivot, end):
    pass






if __name__ == '__main__':
    unsorted = [3,345,456,7,879,970,7,4,23,123,45,467,578,78,6,4,324,145,345,3456,567,5768,6589,69,69]
    sort = quicksort(unsorted)

    print '%r <-- unsorted' % unsorted
    print '%r <-- sorted' % sort
