class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:

    def __init__(self, n):

        self.head=Node(n)
        self.last=self.head

    def add(self,n):
        self.last.next=Node(n)
        self.last=self.last.next

    def printList(self):
        temp=self.head
        while (temp):
        
            print(temp.data," ")
            temp=temp.next

    def getIndex(self,n):
        temp=self.head
        i=0
        while (i!=n):
            i+=1
            temp=temp.next
        #print(temp)

        return(temp)

    def addToStart(self,n):
        n.next=self.head
        self.head=n

    def addIn(self,n1,new):
        temp=n1.next
        newNode=Node(new)
        newNode.next=temp
        n1.next=newNode
        if(n1== self.last):
            self.last=n1.next

        # SOLVE FOR self.last variable if the addIn appends to the last

    def delete(self,key):
        
        if( self.head.data == key):
            self.head=None

        else:
            temp=self.head
            while(temp!=None):
                if(temp.next.data == key):
                    temp.next=temp.next.next
                    if(temp.next.next.next==None):
                        self.last=temp.next.next
                    break
                    

                temp=temp.next

        

if __name__=='__main__': 
  
  
    llist = LinkedList(2) 
    llist.add(3)
    llist.add(4)
    llist.add(5)
    
    llist.printList() 