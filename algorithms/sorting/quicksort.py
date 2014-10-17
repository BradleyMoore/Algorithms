from random import randint

def quicksort(unsorted, start=0, end=0):
    if len(unsorted) <= 1:
        return unsorted
        
    pivot = choose_pivot(start, end)
    sorted = sort(unsorted, pivot, start, end)
    
    return sorted
    
    
def choose_pivot(start, end):
    pivot = randint(start, end-1)
    
    return pivot


def sort(unsorted, pivot, start=0, end=len(unsorted)):
    pass
    

def first_half(unsorted, start, end):
    pass


def last_half(unsorted, start, end):
    pass
    
    






if __name__ == '__main__':
    unsorted = [3,345,456,7,879,970,7,4,23,123,45,467,578,78,6,4,324,145,345,3456,567,5768,6589,69,69]
    sort = quicksort(unsorted)

    print '%r <-- unsorted' % unsorted
    print '%r <-- sorted' % sort
