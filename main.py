class SortedCollection:
  def __init__(self):
    self.list = []
    

  
  def add(self, num):
    self.list.insert(self.__findSlot(num), num)


  def __findSlot(self, num):
    i = 0
    while i < len(self.list) and self.list[i] < num:
      i+=1
    return i
  
    
    
  def printContents(self):
    print(self.list)

list = SortedCollection()
list.add(7)
list.printContents()
list.add(1)
list.printContents()
list.add(3)
list.printContents()
list.add(12)
list.printContents()
list.add(9)
list.printContents()
list.add(7)
list.printContents()

  