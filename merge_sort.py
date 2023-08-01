def merge_sort(list: list):
    """
    Sort Array in Ascending Order

    Algorithm - Divide And Conquer
    
    Divide - Split list into sublist (left, right) until the length of the list is 1
    Conquer - Recursively sort the merge list created in the previous section
    Combine - Merge the left and right side of the splitted list

    Takes overall O(kn log n) - Quasalinear runtime
    """

    if len(list) == 1: return list

    left_half,right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)



def split(list):
    """
    Divide list into two from the middle of the list (left half and right half)
    Return the left half, right half

    Takes over all O(k log n) - Logarithmic runtime
    note k = slice size
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right



def merge(left: list, right: list):
    """
      merge two list together in ascending order
      return the sorted list

      Takes over all O(n) - Linear runtime
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    # incase the left list length is greater the right list length
    l = l + left[i:]
    # incase the right list length is greater the left list length
    l = l + right[j:]


    return l


def verify_sort(list):
    """
    check if list is sorted

    Takes O(n) - Linear runtime
    """
    if len(list) == 1 : return True
    return (list[0] <= list[1]) and verify_sort(list[1:])


list = [10,47,78,3,23,11,67,43,33]
sortedList = merge_sort(list)

# print(verify_sort(list))
print(verify_sort(sortedList))
