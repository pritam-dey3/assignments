class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

    def append(self,v):
        if (self.value == None):
            self.value = v
        elif (self.next == None):
            self.next = Node(v)
        else:
            self.next.append(v)

    def insert(self,v):
        if (self.value == None):
            self.value = v
        else:
            newNode = Node(v)
            (self.value,newNode.value) = (newNode.value,self.value)
            (self.next,newNode.next) = (newNode,self.next)

    def show(self):
        if(self.next == None):
            print(str(self.value))     
        else:
            print(str(self.value),end=", ")
            self.next.show()

    def delete(self,v):
        if(self.value == None):
            print("Nothing found")
        if(self.value == v):
            self.value = None
            if(self.next != None):
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if(self.next != None):
                self.next.delete(v)
                if(self.next.value == None):
                    self.next = None
        return

    def length(self):
        if self.value == None:
          return(0)
        elif self.next == None:
          return(1)
        else:
          return(1+self.next.length())

def run():
    a = Node(5)
    for i in range(5):
        a.append(i)
    return a

                    
                









            
