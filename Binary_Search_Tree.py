import re

class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1
      
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None
    # TODO complete initialization
  
  def __set_height(self, node):
    x = 0
    y = 0
    if node.right is not None:
      x = node.right.height
    if node.left is not None:
      y = node.left.height
    if x >= y:
      node.height = x + 1
    elif y > x:
      node.height = y + 1
    

  def __balance(self, sub):
    rh = 0
    lh = 0
    if sub.right is not None:
      rh = sub.right.height
    if sub.left is not None:
      lh = sub.left.height
    balance = rh - lh
    if sub is None:
      return sub
    if balance == -2:
      crh = 0
      clh = 0
      if sub.left is not None:
        if sub.left.right is not None:
          crh = sub.left.right.height
        if sub.left.left is not None:
          clh = sub.left.left.height
      childbalance = crh - clh
      if childbalance > 0:
        fix = sub.left.right
        fixfloater = fix.left
        fix.left = sub.left
        sub.left = fix
        fix.left.right = fixfloater

        #Fix Subtree Height Calc
        Binary_Search_Tree.__set_height(self, fix.left)

        #Fix Height Calc
        Binary_Search_Tree.__set_height(self, fix)

      newroot = sub.left
      floater = newroot.right
      newroot.right = sub
      sub.left = floater

      #Newroot Subtree Height Calc
      Binary_Search_Tree.__set_height(self, newroot.right)

      #Newroot Height Calc
      Binary_Search_Tree.__set_height(self, newroot)

      return newroot

    if balance == 2:
      crh = 0
      clh = 0
      if sub.right is not None:
        if sub.right.right is not None:
          crh = sub.right.right.height
        if sub.right.left is not None:
          clh = sub.right.left.height
      childbalance = crh - clh
      if childbalance < 0:
        fix = sub.right.left
        fixfloater = fix.right
        fix.right = sub.right
        sub.right = fix
        fix.right.left = fixfloater

        #Fix Subtree Height Calc
        Binary_Search_Tree.__set_height(self, fix.right)

        #Fix Height Calc
        Binary_Search_Tree.__set_height(self, fix)

      newroot = sub.right
      floater = newroot.left
      newroot.left = sub
      sub.right = floater

      #Newroot Subtree Height Calc
      Binary_Search_Tree.__set_height(self, newroot.left)

      #Newroot Height Calc
      Binary_Search_Tree.__set_height(self, newroot)
        
      return newroot


    #Height Calc
    Binary_Search_Tree.__set_height(self, sub)

    return sub


  def __recursive_insert(self, x, sub):
    if sub == None:
      new = Binary_Search_Tree.__BST_Node(x)
      return new
    if x < sub.value:
      sub.left = Binary_Search_Tree.__recursive_insert(self, x, sub.left)
    if x > sub.value:
      sub.right = Binary_Search_Tree.__recursive_insert(self, x, sub.right)
    if x == sub.value:
      raise ValueError("Value already exists")

    return self.__balance(sub)

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = Binary_Search_Tree.__recursive_insert(self, value, self.__root)


  def __recursive_remove(self, x, sub):
    if sub == None:
      raise ValueError("The Value is Missing")
    if sub.value == x:
      if (sub.left == None) and (sub.right == None):
        return None
      elif (sub.left == None) and (sub.right != None):
        return sub.right
      elif (sub.left != None) and (sub.right == None):
        return sub.left
      else:
        cur = sub.right
        while cur.left is not None:
          cur = cur.left
        sub.value = cur.value
        sub.right = Binary_Search_Tree.__recursive_remove(self, cur.value, sub.right)
        return self.__balance(sub)

    if x < sub.value:
      sub.left = Binary_Search_Tree.__recursive_remove(self, x, sub.left)
    if x > sub.value:
      sub.right = Binary_Search_Tree.__recursive_remove(self, x, sub.right)
    
    return self.__balance(sub)


  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = Binary_Search_Tree.__recursive_remove(self, value, self.__root) 
  
  def __in_order_traversal(self, node):
    res = []
    if node is not None:
      res = res + self.__in_order_traversal(node.left)
      res.append(node.value)
      res = res + self.__in_order_traversal(node.right)
    return res

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.get_height() == 0:
      return "[ ]"
    sub = Binary_Search_Tree.__in_order_traversal(self, self.__root) 
    output = "[ "
    for i in sub:
      output = output + str(i) + ", "
    output = output[:-2]
    output += " ]"

    return output

  def __pre_order_traversal(self, node):
    res = []
    if node is not None:
      res.append(node.value)
      res = res + self.__pre_order_traversal(node.left)
      res = res + self.__pre_order_traversal(node.right)
      
    return res

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.get_height() == 0:
      return "[ ]"
    sub = Binary_Search_Tree.__pre_order_traversal(self, self.__root) 
    output = "[ "
    for i in sub:
      output = output + str(i) + ", "
    output = output[:-2]
    output += " ]"

    return output
  
  def __post_order_traversal(self, node):
    res = []
    if node is not None:
      res = res + self.__post_order_traversal(node.left)
      res = res + self.__post_order_traversal(node.right)
      res.append(node.value) 
    
    return res

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.get_height() == 0:
      return "[ ]"
    sub = Binary_Search_Tree.__post_order_traversal(self, self.__root) 
    output = "[ "
    for i in sub:
      output = output + str(i) + ", "
    output = output[:-2]
    output += " ]"

    return output
  

  def to_list(self):
    return Binary_Search_Tree.__in_order_traversal(self, self.__root) 


  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root is None:
      return 0
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  x = Binary_Search_Tree()
  x.insert_element(23)
  x.insert_element(15)
  x.insert_element(94)
  x.insert_element(72)
  x.insert_element(81)
  x.insert_element(105)
  x.insert_element(74)
  x.insert_element(78)
  x.insert_element(12)
  x.insert_element(65)
  x.insert_element(87)
  x.insert_element(85)
  x.insert_element(41)
  x.insert_element(52)
  x.insert_element(45)
  x.insert_element(56)
  x.insert_element(53)
  print(x)
  print(x.pre_order())
  print(x.post_order())

 


  

