class twoStacks:

  def __init__(self,size):
    self.size=size
    self.top=-1
    self.last=size
    self.arr=[None]*size
    

  def pop1(self):
    if(self.top!=-1):
      self.top-=1
      return(self.arr[self.top+1])

    else:
      print("Stack Underflow")
    

  def pop2(self):
    if(self.last!=self.size):
      self.last+=1
      return(self.arr[self.last-1])

    else:
      print("Stack Underflow")
    
  def push1(self,n):
    if(self.top+1==self.last):
      print("Stack is full")

    else:
      self.arr[self.top+1]=n
      self.top+=1

  def push2(self,n):
    if(self.top+1==self.last):
      print("Stack is full")
    else:
      self.arr[self.last-1]=n
      self.last-=1
    
    
  def printst(self):
    print(self.arr[: self.top+1])
    print(self.arr[self.last:])
    

if __name__ == '__main__':

  st=twoStacks(10)
  st.push1(1)
  st.push1(1)
  st.push1(1)
  st.push1(1)
  st.push1(1)
  st.push2(2)
  st.push2(2)
  st.push2(2)
  st.push2(2)
  st.push2(2)
  st.push2(2)

  st.printst()
  st.pop1()
  st.printst()

  st.push2(2)
  st.printst()
  st.pop1()
  st.pop1()
  st.pop1()
  st.pop1()

  st.pop1()
  st.push1(3)
  st.push2(4)
  st.printst()

  st.push1(5)
  st.push1(5)
  st.printst()
  
