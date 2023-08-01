def quicksort(list: list):
    """
      Sorting list based on pivot (selecting the first item) 
      split list into sublist -> the number less than the pivot and numbers greater
    """

    if len(list) <= 1: return list

    pivot = list[0]
    sliced_list = list[1:]

    items_less_than_pivot = []
    items_greater_than_pivot = []

    for i in range(0, len(list[1:])):
        if(sliced_list[i] < pivot): items_less_than_pivot.append(sliced_list[i])
        else: items_greater_than_pivot.append(sliced_list[i])
    # print("%25s %s %-25s" % (items_less_than_pivot, pivot, items_greater_than_pivot))
    return quicksort(items_less_than_pivot) + [pivot] + quicksort(items_greater_than_pivot)


numbers = [10,47,78,3,23,11,67,43,33]

def verify_sort(list):
    """
    Check if list is sorted
    Takes O(n) - Linear runtime
    """
    if len(list) == 1 : return True
    return (list[0] <= list[1]) and verify_sort(list[1:])

print(verify_sort(quicksort(numbers)))