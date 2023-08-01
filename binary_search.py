def binary_search(list, target):
    first_index = 0
    last_index = len(list) - 1

    while first_index <= last_index:
        midpoint = (first_index + last_index) // 2
        
        if(list[midpoint] == target):
          return midpoint
        elif(list[midpoint] > target):
          last_index = midpoint -1
        else: first_index = midpoint + 1
    
    return None


def verify(index):
    if index is not None: 
        print(f"The target index is: {index}")
    else: print("Target index not found")


numbers = [1,2,3,4,5,6,7,8,9,10]

verify(binary_search(numbers, 7))
verify(binary_search(numbers, 12))