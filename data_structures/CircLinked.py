# THIS IS CIRCULAR DOUBLE LINKEDLIST

class Node:
  def __init__(self,value):
    self.value=value
    self.prev=None
    self.next=None

class CircLinked:

  def __init__(self,value,boo=False):
    if(boo):
      self.head=value
      self.last=self.head.prev
    else:
      self.head=Node(value)
      self.last=self.head
      self.last.next=self.head
      self.head.prev=self.last

  def append(self,value):
    n=Node(value)
    self.last.next=n
    n.prev=self.last
    n.next=self.head
    self.head.prev=n
    self.last=n

  def print(self):
    temp=self.head
    i=None
    while(temp!=i):
      print(temp.value)
      temp=temp.next
      
      i=self.head

  def reversePrint(self):
    temp=self.last
    i=0
    while(i<10):
      print(temp.value)
      temp=temp.prev
      i+=1

  def split(self,loc):
    temp=self.head
    i=0
    while(True):
      if(i==loc):
        temp1=self.last
        temp1.next=temp.next
        temp.next.prev=temp1

        self.last=temp
        temp.next=self.head
        self.head.prev=temp

        cll2=CircLinked(temp.next,True)
        #print(cll2.head.value)
        return([self,cll2])
      i=i+1
      temp=temp.next

if __name__ == '__main1__':
  ll=CircLinked(0)
  ll.append(1)
  ll.append(2)
  ll.append(3)
  ll.append(4)
  ll.append(8)
  #ll.print()
  ll.reversePrint()

  s=ll.split(4)
  print('\n')
  print(s[1].print())
  print('\n','Reverse Print')
  ll.reversePrint()

if __name__=='__main__':
  ll=CircLinked(0)
  ll.append(1)
  ll.append(2)
  ll.append(3)
  ll.append(4)
  ll.append(8)

  Node1=ll.head
  CircLinked(Node1,True).reversePrint()
