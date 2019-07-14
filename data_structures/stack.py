class Node:
  def __init__(self,val):
    self.value=val
    self.next=None

class Stack:

  def __init__(self):
    self.root=None

  def push(self,val):
    value=Node(val)
    t=self.root
    self.root=value
    value.next=t
    
  def pop(self):
    if(self.root!=None):
      t=self.root.next
      self.root=t
    
    else:
      print('Nothing to pop!')

  def isEmpty(self):
    return(self.root==None)

  def peek(self):
    if(self.isEmpty()==False):
      print(self.root.value)
    else:
      print('No Element to peek')

  def print(self):
    temp=self.root
    while(temp!=None):
      print(temp.value)
      temp=temp.next

if __name__ == '__main__':

  s=Stack()
  s.push(0)
  s.push(1)
  s.push(2)
  s.push(3)
  s.push(4)
  s.push(5)
  s.push(6)
  s.pop()
  s.peek()
  s.print()


