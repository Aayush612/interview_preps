class Node:
  def __init__(self,value):
    self.next=None
    self.prev=None
    self.data=value

class DLinked:
  def __init__(self,value):
    self.head=Node(value)
    self.last=self.head

  def push(self, value):
    temp=Node(value)
    self.last.next=temp
    temp.prev=self.last
    self.last=temp

  def print(self):
    temp=self.head
    while(temp!=None):
      print(temp.data," ")
      temp=temp.next

  def printRev(self):
    temp=self.last
    while(temp!=None):
      print(temp.data)
      temp=temp.prev

  def addAfter(self,value1,newvalue):
    temp=self.head
    while(temp!=None):
      if(temp.data==value1):
        if(temp!=self.last):
          temp1=temp.next
          temp.next=Node(newvalue)
          temp.next.prev=temp
          temp.next.next=temp1
          temp.next.next.prev=temp.next
        else:
          temp.next=Node(newvalue)
          temp.next.prev=temp
          self.last=temp.next
        break
      temp=temp.next
  
  def reverse(self):

    temp=self.head
    while(temp!=None):
      t=temp.next
      temp.next=temp.prev
      temp.prev=t
      temp=temp.prev

    temp=self.head
    self.head=self.last
    self.last=temp


if __name__ == '__main__':
  ll=DLinked(1)
  ll.push(2)
  ll.push(3)
  ll.push(4)
  ll.push(5)
  ll.print()






