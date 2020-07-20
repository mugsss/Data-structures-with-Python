# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:09:50 2020

@author: Mugdha
"""

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
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
        print("The elements are:")
        msg = []
        temp = self.__head
        while(temp!= None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        for i in msg:
            print(i)
    
    def find_node(self,data):
        pass
        temp = self.__head
        while( temp!= None):
            if(temp.get_data() == data):
                return True
            else:
                temp = temp.get_next()
        #Remove pass and write the logic to find the node and return the node if found or return None.
                                            
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
list1.add('milk')
list1.add('teapackets')
list1.add('bread')
list1.add('Sugar')
list1.add('juice')
list1.display()
#Search for the required node

node=list1.find_node("Sugar")
if(node!=None):
    print("Node found")
else:
    print("Node not found") 
