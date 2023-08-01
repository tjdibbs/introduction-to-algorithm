from linkedlist import LinkedList, Node


def linked_list_merge_sort(list: LinkedList):
    """
    Sort Array in Ascending Order

    Algorithm - Divide And Conquer
    
    Divide - Split list into sublist (left, right) until the length of the list is 1
    Conquer - Recursively sort the merge list created in the previous section
    Combine - Merge the left and right side of the splitted list

    Takes overall O(kn log n) - Quasalinear runtime
    """

    if not list.head or list.size() <= 1: return list

    print({"list": list})

    left_half,right_half = split(list)
    left = linked_list_merge_sort(left_half)
    right = linked_list_merge_sort(right_half)

    # print({"left": left, "right": right})
    return merge(left, right)


def split(list: LinkedList):
    """
    Divide list into two from the middle of the list (left half and right half)
    Return the left half, right half

    Takes over all O(k log n) - Logarithmic runtime
    note k = slice size
    """

    """ What I did before checking video """
    # mid_point = list.size()//2
    # mid_node = list.getItem(mid_point)

    # left = LinkedList()
    # left.head = list.head

    # last_node: Node = left.getItem(mid_point - 1)
    # print({last_node, list.size()})

    # if last_node is not None: last_node.next_node = None

    # right = LinkedList()
    # right.head = mid_node


    mid_point = list.size()//2
    mid_node = list.getItem(mid_point - 1)
    
    left = list

    right = LinkedList()
    right.head = mid_node.next_node

    mid_node.next_node = None

    return left, right



def merge(left: LinkedList, right: LinkedList):
    """
      - merge two linked list together in ascending order by comparing data in node
      - return the sorted linked list
      - Takes over all O(n) - Linear runtime
    """

    print({"left": left, "right": right})

    merged = LinkedList()

    """fakes head that will be removed at the end"""
    merged.add(0)

    # i = left.head
    # j = right.head

    # last_node = l.head

    # while i and j:
    #     """ Get the last item in linked list """
    #     last_node = l.getItem(l.size() - 1)
    #     if i.data < j.data:
            
    #         next_node = i.next_node
    #         i.next_node = None

    #         if l.head is not None: last_node.next_node = i 
    #         else: 
    #             l.head = i
    #             last_node = i

    #         i = next_node
    #     else:
    #         next_node = j.next_node
    #         j.next_node = None

    #         if l.head is not None: last_node.next_node = j 
    #         else: l.head = j

    #         j = next_node
    

    # # incase the left list length is greater the right list length
    # while i:
    #     next_node = i.next_node
    #     i.next_node = None

    #     last_node = l.getItem(l.size() - 1)
    #     last_node.next_node = i
    #     i = next_node

    # # incase the right list length is greater the left list length
    # while j:
        # next_node = j.next_node
        # j.next_node = None

        # last_node = l.getItem(l.size() - 1)
        # last_node.next_node = j
        # j = next_node

    left_head = left.head
    right_head = right.head

    current = merged.head

    while left_head or right_head:
        """ 
        Since it is possible for left_head or right_head to be None, 
        then we have to check for that
        """
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node

        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node

        else:
          if left_head.data < right_head.data:
              current.next_node = left_head
              left_head = left_head.next_node
          else:
              current.next_node = right_head
              right_head = right_head.next_node

        current = current.next_node
    
    merged.remove(0)
    return merged


def verify_sort(list):
    """
    check if list is sorted

    Takes O(n) - Linear runtime
    """
    if len(list) == 1 : return True
    return (list[0] <= list[1]) and verify_sort(list[1:])


list = LinkedList()
list.add(10).add(1).add(30).add(12).add(4)

sortedList = linked_list_merge_sort(list)


print(sortedList)



x = {"name": "james"}
b = x['name']

x["name"] = "time"

print({"x": x, "b": b})