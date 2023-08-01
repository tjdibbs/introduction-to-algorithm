def recursive_binary_search(list, target):
    if len(list) == 0:
        return False

    midpoint = (len(list)) // 2

    if list[midpoint] == target:
        return midpoint
   
  #  This type of recursion is called Tail Recursion. And Where Tail Optimizations comes in
    return recursive_binary_search(
        list[midpoint+1:] if list[midpoint] < target else list[:midpoint],
        target
    )



def verify(found):
     print(f"The target index is: {found}")


numbers = [1,2,3,4,5,6,7,8,9,10]

verify(recursive_binary_search(numbers, 7))
verify(recursive_binary_search(numbers, 12))