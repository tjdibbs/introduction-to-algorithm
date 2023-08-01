class Node:
   def __init__(self, data):    
    self.next_node = None
    self.data = data

   def __repr__(self):
    return "<Node: %d>" % self.data
   

class LinkedList:
  head: Node

  def __init__(self):
    self.head = None
  

  def size(self):
    count = 0
    current_node = self.head
    while current_node:
      current_node = current_node.next_node
      count+=1

    return count

  def add(self, item: int):
    """ 
      Add new item to the LinkedList
    """

    newItem = Node(item)
    newItem.next_node = self.head

    self.head = newItem

    return self


  def remove(self, key: int):
    """
      remove item data that matched the key provided
      return the item if found otherwise Node
      Takes O(n) times - Linear runtime
    """

    # check the head of the list first
    if self.head.data == key:
        self.head = self.head.next_node
        return
    
    current_node = self.head
    previous_node: Node = None

    while current_node:
      if current_node.data == key:
        previous_node.next_node = current_node.next_node
        return current_node
      else:
        previous_node = current_node
        current_node = current_node.next_node

    return None


  def search(self, key: int):
    count = 0  
    current_node = self.head

    while current_node:
      if current_node.data == key:
        return current_node
      current_node = current_node.next_node
      count+=1

    return None


  def getItem(self, index: int):
    count = 0  
    current_node = self.head

    while current_node:
      if count == index:
        return current_node
      current_node = current_node.next_node
      count+=1

    return None

  def __repr__(self) -> str:
    """
      modify the representation of the LinkedList class  
    """

    listItems = []
    current = self.head

    while current:

      prefix = "head: " if current == self.head else ""
      prefix = "tail: " if not current.next_node else prefix

      listItems.append(f"[{prefix + str(current.data)}]")
      current = current.next_node

    return f"<LinkedList: {'-> '.join(listItems)}>"