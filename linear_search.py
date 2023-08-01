def linear_search(list, target):
    index = 0
    while len(list) > index:
        if(list[index] == target):
            return index
        index += 1
    return None


def verify(index):
    if index is not None: 
        print(f"The target index is: {index}")
    else: print("Target index not found")


numbers = [1,2,3,4,5,6,7,8,9,10]

verify(linear_search(numbers, 7))
verify(linear_search(numbers, 12))