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
      popped=self.root
      t=self.root.next
      self.root=t
      return(popped)

    else:
      print('Nothing to pop!')

  def isEmpty(self):
    return(self.root==None)

  def peek(self):
    if(self.isEmpty()==False):
      #print(self.root.value)
      return(self.root.value)
    else:
      print('No Element to peek')

  def print(self):
    temp=self.root
    while(temp!=None):
      print(temp.value)
      temp=temp.next

def check(s):
  op=['{','(','[','<']
  cl=['}',')',']','>']
  stac=Stack()
  for char in s:
    if(char in op):
      stac.push(char)
    elif char in cl:
      if(stac.peek()==op[cl.index(char)]):
        stac.pop()
      else:
        print("Wrong")
        return
  
  if(stac.isEmpty()):
    print("Verified")

  else:
    print("Bracket not closed")



if __name__ == '__main__':
  inp=input("Enter Brackets")
  check(inp)
  

