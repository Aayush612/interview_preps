class Node:
  def __init__(self,name,value):
    self.l=None
    self.r=None
    #self.l.name=None
    #self.r.name=None
    self.name=name
    self.value=value
    self.arr=[self.l,self.r]

class Tree:

  def __init__(self,name,value):
    self.root=Node(name,value)

  def add(self,name,value,address):
    N=find(address) #return Node
    if(N.l==None):
      N.l=Node(name,value)
    else:
      N.r=Node(name,value)

  def find(self,address):
    s_add=address.split('/')
    i=0
    point=[self.root.name]

    while(True):
      try:
        if(s_add[i] in point):
          selected=point.index(s_add[i])
          point=selected.arr[selected.arr!=None]
          i+=1
          if(point==[None,None] and i==len(s_add)):
            return selected

          elif(i==len(s_add)):
            print('address wrong')
            break

          else:
            print('address incomplete')
            break
        
        else:
          print('adress wrong from here')
          for ad in s_add[i]:
            print(ad,'/')
          break
      except:
        print("Exception")

if __name__ == '__main__':

  tree=Tree('A',12)
  tree.add('A')


        
          


    
