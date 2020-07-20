#Insert new node after an old node(data)  

class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        item = Node(data)
        if(self.__head == None):
            self.__head = item
            self.__tail = item
        else:
            self.__tail.set_next(item)
            self.__tail = item
    
    def display(self):
        print("The final linked List")
        temp = self.__head
        msg = []
        while(temp!=None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        for i in msg:
            print(i)
            
    def find_node(self,data):
        temp = self.__head
        while(temp != None):
            if(temp.get_data()==data):
                return temp
            else:
                temp = temp.get_next()
                
        
    def insert(self,data,data_before):
        item = Node(data)
        temp = list1.find_node(data_before)
        if(temp==None):
            print("The old node with this "+ data_before+ " does not exist")

        elif(temp.get_next() == None):
            print("The new node with "+data+ " is added after old node with "+data_before+ " to linked list")
            temp.set_next(item)
            self.__tail = item
        else:
            print("The new node with "+data+ " is added after old node with "+data_before+ " to linked list")
            item.set_next(temp.get_next())
            temp.set_next(item)                                          
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
#Add all the required element(s)
list1.add("Teabags")
list1.add("Biscuits")
list1.add("lemons")
list1.add("Sugar")

#Insert the element in the required position
#It accepts the data in the node to be inserted and the data in the node after which the new node should be inserted.
#list1.insert("NewItem","Sugar")

list1.insert("Salt","Biscuits")
list1.insert("Pasta","Sugar")
list1.insert("Juice","Soap")
list1.display()
                                              
