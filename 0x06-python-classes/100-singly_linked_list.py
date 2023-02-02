#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    
    """ retrieves the private instance data attribute """
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        val = ""
        temp = self.__head
        while temp is not None:
            val += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                val += "\n"
        return val

    def sorted_insert(self, value):
        new_val = Node(value)
        if self.__head is None:
            self.__head == new_val
            return

        temp = self.__head
        if new_val.data < temp.data:
            new_val.next_node = self.__head
            self.__head = new_val
            return

        while ((temp.next_node is not None) and (new_val.data > temp.next_node.data)):
            temp = temp.next_node
        new_val.next_node = temp.next_node
        temp.next_node = new_val
        return
