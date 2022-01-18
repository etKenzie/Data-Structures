class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.data = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        if self.__header.next is self.__trailer:
            result = 0
        if self.__header.next is not self.__trailer:
            result = 1
            current = self.__header.next
            while current.next is not self.__trailer:
                result = result + 1
                current = current.next
        self.__size = result

        

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    ## Function to discover if index at first or second half
    def __half(self, place):
        if(place<=(self.__size/2)):
            return True
        else:
            return False

    def __walk(self, position):
        if(Linked_List.__half(self, position) is True):
            current = self.__header
            for i in range(0, position):
                current = current.next
        else:
            current = self.__trailer.prev
            for i in range(len(self) - position-1):
                current = current.prev
        return current
        
    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        newest = Linked_List.__Node(val)
        
        newest.next = self.__trailer
        self.__trailer.prev.next = newest
        newest.prev = self.__trailer.prev  
        self.__trailer.prev = newest
            
        self.__size = self.__size + 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        if index >= len(self) or index < 0:
            raise IndexError("invalid index")
            return
        newest = Linked_List.__Node(val)
        # Determine if top or bottom half then current Walk to index
        current = Linked_List.__walk(self, index)
        if(Linked_List.__half(self, index) is True):
            newest.next = current.next
            current.next = newest
            newest.next.prev = newest
            newest.prev = current
            
        else:
            newest.prev = current.prev
            current.prev = newest
            newest.prev.next = newest
            newest.next = current
            
        self.__size = self.__size + 1



    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if index >= len(self) or index < 0:
            raise IndexError("invalid index")
            return
        if len(self) == 0:
            print("list is empty")
            return
        # Determine if top or bottom half then current Walk to index
        current = Linked_List.__walk(self, index)
        if(Linked_List.__half(self, index) is True):
            item = current.next.data
            current.next = current.next.next
            current.next.prev = current 
        else:
            current = current.next
            item = current.prev.data
            current.prev = current.prev.prev
            current.prev.next = current
        self.__size = self.__size - 1
        return item

        
        

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index >= self.__size or index < 0:
            raise IndexError("invalid index")
            return
        if self.__size == 0:
            print("list is empty")
            return
        # Determine if top or bottom half then current Walk to index
        current = Linked_List.__walk(self, index)
        current = current.next
        element = current.data
        return element

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if len(self) <= 1:
            return
        current = self.__header.next
        current.prev = self.__trailer.prev
        self.__trailer.prev = current
        self.__header.next = self.__header.next.next
        self.__trailer.prev.prev.next = current
        self.__trailer.prev.next = self.__trailer
        self.__header.next.prev = self.__header
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        if(len(self)==0):
            return "[ ]"
        current = self.__header.next
        output = "[ "
        for i in range(len(self)):
            output = output + str(current.data) + ", "
            current = current.next
        # Used to take out the aditional ", " that appears at the end of string
        output = output[:-2]
        output += " ]"
        return output

    def __iter__(self):
        ''' We want this method to return an iterator (an object that successively yields the next item contained by our object)'''
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
#         current = self._header._next
#         while current._next is not self._trailer:
#             # Here in the first pass we yield the current data. 
#             # We use yeild because we don't want to save so many values in memory and we want it to be temporary.
#             # We also need to return a generator object at each iteration step before we see the trailer
#             yield current._data
#             current = current._next
        self.__start = self.__header.next
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        
        # Have to create a temporary variable here to offset by 1
        if (self.__start is self.__trailer):
            raise StopIteration
        
        
        result = self.__start.data
        # Updating current node of the self object to adjacent one
        self.__start = self.__start.next
        return result

    def __reversed__(self): ## are we supposed to make a new linked list or just return a backwards string?
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        new = Linked_List()
        current = self.__trailer.prev
        while current is not self.__header:
            new.append_element(current.data)
            current = current.prev
        return new

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    a = Linked_List()
    
    # Make sure string of empty list is correct
    try:
        print(a)
        assert str(a) == "[  ]"
    except AssertionError:
        print ("String of a is not formated right")

    # Empty Len Check
    try:
        assert len(a) == 0
    except AssertionError:
        print ("Error: the length of the string is meant to be 0")



    try: # these should all cause Index Errors
        a.get_element_at(4)
        a.get_element_at(2)
    except IndexError:
        print('Correctly Caught Invalid Index, as the list is still empty')
    
    try: # these should work without error
        a.append_element(0)
        assert len(a) == 1
    except IndexError:
        print('Error: Should not Raise IndexError as only appending')
    except AssertionError:
        print("Error: Should not raise assertion error as len of list should be 1")
    print(a)
    print('list has indexes 0 to ' + str(len(a)-1))

    try: # these should all work without error
        a.append_element(1)
        a.append_element(2)
        a.append_element(3)
        a.append_element(-4)
        # making sure the length of list is correct
        assert len(a) == 5
    except IndexError:
        print('Error: Should not Raise IndexError as only appending')
    except AssertionError:
        print("Error: Should not raise assertion error as len of list should be 5")
    print(a)
    print('list has indexes 0 to ' + str(len(a)-1))

    try: # list of size 5 so indexes 0-4
        a.get_element_at(5)
    except IndexError:
        print('Correctly Caught Invalid Index 5, as the list only goes to index 4')


    ## Iterator Check
    try:
        b = []
        for val in a:
            b.append(val)
        assert b == [0,1,2,3,-4]
    except AssertionError:
        print("Error: iteration does not work")

    ## String Check
    try:
        assert str(a) == "[ 0, 1, 2, 3, -4 ]"
    except AssertionError:
        print("Error: the string is not as its supposed to be formated")

    
    try: # Should cause Index Errors
        a.insert_element_at(5,5)
    except IndexError:
        print('Correctly Caught Invalid Index, as the list only goes to index 4')
    except AssertionError:
        print("Error: the string is not as its supposed to be formated")

    #Check if inserting item at invalid index changes the list
    try:
        assert str(a) == "[ 0, 1, 2, 3, -4 ]"
    except AssertionError:
        print("Error: the string is not as its supposed to be formated")

    ## Check to see valid Index Input and length of list increased
    try:
        a.insert_element_at(100,3)
        assert a.get_element_at(3) == 100
        assert len(a) == 6
    except AssertionError:
        print("Error: the third element of the list is not 100 when I just inserted 100 to the third index or wrong length of list")
    

    ## See if Correct Remove Element and length of list reduced
    try:
        a.remove_element_at(3)
        assert a.get_element_at(3) != 100
        assert len(a) == 5
    except AssertionError:
        print("Error: the third element is not supposed to be 100 as it was just removed or wrong length of list")
    
    
    ## Testing wrong index for remove element
    try:
        a.remove_element_at(20)
    except IndexError:
        print("Correctly caught that there is no index 20 in this list")
    # Check that list remains unchanged 
    try:
        assert str(a) == "[ 0, 1, 2, 3, -4 ]"
    except AssertionError:
        print("Error: the string should have remained unchanged")


    ## Reversed Iterator Check
    try:
        c = []
        for val in reversed(a):
            c.append(val)
        assert c == [-4,3,2,1,0]
    except AssertionError:
        print("Error: reversed iteration does not work")

## Testing rotate left
    try:
        a.rotate_left()
        assert str(a) == "[ 1, 2, 3, -4, 0 ]"
    except AssertionError:
        print("Error: the string should be changed accordingly")

