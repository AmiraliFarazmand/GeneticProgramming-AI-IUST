# # imports:
# from  random import randint ,choice ,random


# # global variables:
# operators_list =list(["+" , "-" , "/" , "*" , "**" ,"sin" , "cos" , "tan" , "cot" , "exp"])
# unery_operators_list =list(["sin" , "cos" , "tan" , "cot" , "exp" ])
# binary_operators_list =list(["+" , "-" , "/" , "*" , "**"])
# # user's values:
# users_variables = ["x"]             #what variables our function does have
# min_operatos_num = 1                #determine how many operators do we need in our function(create n operators between these 2 variables.)
# max_operatos_num =3
# variable_or_constant_factor = 0.3   #a factor that determines to use constant or a variale in leaf node of the tree .the closer value to 0 the more constants will appear in your function.(must be between 0 and1)
# depth_or_breadth_factor = 0.5       #a factor that determines to fill both sides of the operator on not. the more closer to 0 tree will get filled in breadth not depth. (must be between 0 and1)
#                                     # for example: closer to 0: (((x*10)+2)-5)/3      closer to 1: ((x*10)+2) - ((x-5)\3)
# min_constant_limit = 0              #determine that constants must be in what period.
# max_constant_limit =10            
# class Node():
#     def __init__(self , new_value=None , used=0, father=None , right=None ,left=None , depth = 0 ):
#         self.father =father
#         self.right = right
#         self.left = left
#         self.depth =depth
#         self.used = used
#         self._value = new_value
#         # self.is_operator = new_value in operators_list
#         self.is_op()
#         self.is_binary_op()
    
#     def set_random_op(self):
#         self.value = choice(operators_list)
#     def is_binary_op(self):
#         self.is_binary = self.value in binary_operators_list
#     def is_op(self  ):
#         self.is_operator = self.value in operators_list
    
#     @property
#     def value(self):
#         return self._value 
#     @value.setter
#     def value(self, new_value):
#         # self.is_binary_op()
#         # self.is_op()
#         self.is_binary = new_value in binary_operators_list
#         self.is_operator = new_value in operators_list
#         self._value = new_value
        
#     def __repr__(self) -> str:
#         return f"(V:{self.value} L:{self.left} R:{self.right})"
#     def __str__(self) -> str:
#         if self.left == None and self.right==None :                                          #constant or variable
#             return str(self.value)
#         elif self.value in binary_operators_list:                                            #binary operator
#             return  f"({self.left} {self.value} {self.right})"
#         else:                                                                                #unary operator                                        
#             return f"{self.value} ({self.left}) "
#         # -------------------------------------------------------------------------------------------------------------------------------------
# class Tree():
#     def __init__(self ,  root:Node , nodes:set , MSE = 100000 ):
#         self.root = root 
#         self.MSE = MSE
#         self.nodes = set(nodes)
#         self.nodes.add(root)
#     def add_left_child(self , father_node:Node , left_val:str):
#         left_node  = Node(value=left_val ,father = father_node)
#         father_node.left = left_node
#         left_node.depth = father_node.depth +1
#         self.nodes.add(left_node)
#     def add_right_child(self , father_node:Node , right_val:str):
#         right_node = Node(value=right_val, father = father_node)
#         father_node.right = right_node
#         right_node.depth  = father_node.depth +1
#         self.nodes.add(right_node)
#     def __repr__(self) -> str:
#         return f"tree({self.root}) "
# # -----------------------------------------------------------------------------------------------------------------------------------------------------
# def create_random_tree():
#     num_of_ops = randint(min_operatos_num , max_operatos_num)
#     unattached_nodes =list([Node() for _ in range(num_of_ops-1)])
#     root_node = Node(father="is_root",used=0 ,depth=0,new_value=choice(binary_operators_list))          
#     attached_nodes= list([root_node])                                 #a node gets attached when it has a parent
#     # creating a random tree with operators:
#     print("random shit for test r:",root_node ,"n.o.o:",num_of_ops , "a:", attached_nodes , "u:" , unattached_nodes )
#     while unattached_nodes !=[]:
#         print("***")
#         # **note that: doesn't include the unary operators yet!
#         node =choice(attached_nodes)
#         if node.used == 0:                                     #node is binary operator.
#             if node.value == None:                             #sometimes it is already set in previous loop.
#                 node.value = choice(binary_operators_list)          #**note:needs to change!
#             if node.value in binary_operators_list:
#                 if random()< depth_or_breadth_factor and len(unattached_nodes)>1:          #fill both childs
#                     child1 = unattached_nodes.pop()
#                     child2 = unattached_nodes.pop()
#                     child1.set_random_op()
#                     child2.set_random_op()
#                     node.left =child1
#                     node.right =child2
#                     child2.depth , child1.depth =node.depth +1,node.depth +1
#                     node.used = 1
#                     attached_nodes.append(child1)
#                     attached_nodes.append(child2)
#                 else:                                           #fill one child
#                     child = unattached_nodes.pop()
#                     child.set_random_op()
#                     if random()<0.5:
#                         node.left = child
#                     else:
#                         node.right = child
#                     child.depth =node.depth +1
#                     node.used =1
#                     attached_nodes.append(child)
#             else:                                               #node is unary operator.
#                 child = unattached_nodes.pop()
#                 child.set_random_op()
#                 node.left =child
#                 child.depth =node.depth +1
#                 node.used=1
#                 attached_nodes.append(child)
#     print("after op nodes set: a:" ,attached_nodes ,"u:",unattached_nodes )
#     new_attached_nodes = []
#     # adding values and constants to leaf nodes
#     for node in attached_nodes:
#         print("in second loop; a:" ,attached_nodes ,"u:",unattached_nodes )
#         if node.right ==None :                                  #right node is empty
#             choose_const_or_var = random()
#             if  choose_const_or_var>variable_or_constant_factor:               #fill with constant
#                 temp_value = randint(min_constant_limit , max_constant_limit)
#                 temp_node = Node(new_value=temp_value ,father=node , depth=node.depth+1)
#                 node.right = temp_node
#                 new_attached_nodes.append(temp_node)
#             else:                                               #fill with variable                                  
#                 temp_value = choice(users_variables)
#                 temp_node = Node(new_value=temp_value ,father=node , depth=node.depth+1)
#                 node.right = temp_node
#                 new_attached_nodes.append(temp_node)
#         if node.left ==None :                                   #left node is empty
#             choose_const_or_var = random()
#             if choose_const_or_var>variable_or_constant_factor:               #fill with constant
#                 temp_value = randint(min_constant_limit , max_constant_limit)
#                 temp_node = Node(new_value=temp_value ,father=node , depth=node.depth+1)
#                 node.left = temp_node
#                 new_attached_nodes.append(temp_node)
#             else:                                               #fill with variable                                  
#                 temp_value = choice(users_variables)
#                 temp_node = Node(new_value=temp_value ,father=node , depth=node.depth+1)
#                 node.left = temp_node
#                 new_attached_nodes.append(temp_node)
#     nodes  = set(attached_nodes + new_attached_nodes)
#     print("len:",len(nodes),"nodes:",nodes)
#     temp_tree = Tree(root= root_node ,nodes = nodes)
#     print( "at last a:" ,attached_nodes ,"u:",unattached_nodes )
    
#     return temp_tree
# # ------------------------------------------------------------------------------------------------
# temp_tree = create_random_tree()
"""
dsf
"""
from sklearn.metrics import mean_squared_error
  
# Given values
Y_true = [1,1,2,2,4]  # Y_true = Y (original values)
  
# calculated values
Y_pred = [0.6,1.29,1.99,2.69,3.4]  # Y_pred = Y'
  
# Calculation of Mean Squared Error (MSE)
mean_squared_error(Y_true,Y_pred)