"""
This is an implementation of a singly linked list in python

Resources used:
1. LucidProgramming on youtube: https://www.youtube.com/watch?v=FSsriWQ0qYE&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=5
"""

# Create a class node with the data and next pointer variables

class Node:

	def __init__(self, data):

		self.data = data
		self.next_node = None 


# Singly Linked List

class LinkedList:

	def __init__(self):
		self.head = None


	# Some of the linkedList methods

	def printNodeData(self):
		"""
		Time and space complexities = O(n) because the data might just be 
		in the last node of the linked list
		"""
		# we use the head to track our position in the linked list

		current_node = self.head


		while current_node!=None : # traverse the linked list
			print(current_node.data)

			current_node = current_node.next_node


		

	def searchNode(self, data):
		# should return a boolean True if found or False if not found 
		
		current_node  = self.head

		boolean = False

		while current_node !=None:
			if current_node.data == data:
				boolean = True
				
			else:
				boolean = False

		return boolean

	def appendNode(self, data): # time complexity of O(n)
		new_node = Node(data)

		# Scenario one: The list is empty
		if self.head == None:
			self.head  = new_node
			return

		# Else, if it's not empty move the pointer to the last node of the list
		# Two methods of doint this
		# Method 1
		current_node = self.head

		while current_node != None:
			if current_node.next_node == None: # this is the last node in the list
				current_node.next_node = new_node
				return

			current_node = current_node.next_node

		# # Method 2
		# last_node = self.head

		# while last_node.next_node != None:
		# 	last_node = last_node.next_node

		# last_node.next_node = new_node



	def prependNode(self, data):

		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		current_node = self.head
		self.head = new_node
		new_node.next_node = current_node 

		pass 

	def insertNode(self, data, targetNodeData):

		# Scenarios 1. Linked List is empty, 
		# Scenario 2, traget Node not in the linked list
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		current_node = self.head

		while current_node != None :
			if current_node.data == targetNodeData:
				AfterNode = current_node.next_node
				current_node.next_node = new_node
				new_node.next_node = AfterNode
				return	
			current_node = current_node.next_node


		msg = "Tagert node data {} is not in the linked list".format(targetNodeData)
		return msg

	def deleteNode(self, targetNodeData): # 
		# Assumption made is that the keys are eunique
		# Scenario 1: Linked list is empty
		# scenario 2: Target Node not in the linked list
		# Scenario 3: Deleting the head node

		if self.head is None:
			msg = "Linked List is empty"
			return msg

		current_node = self.head

		# if deleting the head
		if current_node.data == targetNodeData:
			self.head = current_node.next_node
			# Then set the current node to none
			current_node = None
			return

		while current_node.next_node != None: # traverse through the list searching for the target node 
			if current_node.next_node.data == targetNodeData:
				targetNode = current_node.next_node
				beforeTargetNode = current_node
				afterTargetNode = targetNode.next_node
				
				beforeTargetNode.next_node = afterTargetNode
				return

			current_node = current_node.next_node

		# Exit if target node not in the linked list
		msg = "Node {} not in the linked list".format(targetNodeData)
		return msg

	def delByIndex(self, index):

		if self.head is None:
			msg = " Linked list is empty"
			return msg


		current_node = self.head

		if index == 0:
			self.head = current_node.next_node
			current = None
			return

		counter = 1

		while current_node.next_node!= None:
			if counter == index:
				prevNode = current_node
				targetNode = prevNode.next_node
				nexNode = targetNode.next_node

				prevNode.next_node = nexNode
				targetNode = None
				return
			counter += 1
			current_node = current_node.next_node
		msg = "Index not in this list"
		return msg


	def getLength(self): # Iterative
		current_node = self.head
		counter = 0

		while current_node != None:
			counter += 1
			current_node = current_node.next_node 

		return counter


	def NodeSwap(self, input1, input2):

		Node1, Node2 = None, None

		# first check if the inputs are qual ti each other
		if input1 == input2:
			msg = "The nodes to be swapped seems to be equal"
			return msg

		# check if the linked list is empty
		current_node = self.head

		if current_node is None:
			msg = "The linked list is empty"
			return msg

		# Check if the linked list has only one node
		if current_node.next_node is None:
			msg = "This linked list has only one node"
			return msg

		# scenario where one of the inputs is the head node

		if current_node.data == input1:
			prev1 = None
			Node1 = current_node

		if current_node.data == input2:
			prev2 = None
			Node2 = current_node

		while current_node.next_node != None:

			# we check if the data of this node is either of the inputs

			if current_node.next_node.data == input1:
				prev1 = current_node
				Node1 = current_node.next_node

			if current_node.next_node.data == input2:
				prev2 = current_node
				Node2 = current_node.next_node

			current_node = current_node.next_node

		# check if both the inputs were in the linked list
		if Node1 and Node2:
			# Do our swap logic
			# First check if the scenario where one of the nodes to be swapped is the head node
			if prev1 is None:
				self.head = Node2
			else:
				prev1.next_node = Node2

			if prev2 is None:
				self.head = Node1
			else:
				prev2.next_node = Node1

			# swap a,b = b,c //Simple swap in python
			# we know that the next node of Node 1 should point to the next node of Node2 and vice versa
			Node1.next_node, Node2.next_node = Node2.next_node, Node1.next_node

		else:
			msg = "One or all of your inputs were not in linked list"
			return msg



	def nodeSwap_recap(self, input1, input2):

		targetNode1 = None
		targetNode2 = None

		# check if the inputs are equal
		if input1 == input2:
			msg = "Inputs are simillar, cannot swap"
			return msg

		# check if linked list is empty
		current_node = self.head
		if current_node is None:
			msg="Linked list is empty"
			return msg

		# check if linked list has more than one node
		if current_node.next_node is None:
			msg="Linked list has only one node"
			return msg

		# Scenario where one of the inputs is the head  node of the linked list
		if current_node.data == input1:
			prev1 = None
			targetNode1 = current_node

		if current_node.data == input2:
			prev2 = None
			targetNode2 = current_node

		#if none of the inputs is the head node, then traverse the linked list in search of the inputs
		while current_node.next_node is not None:
			print("%%%%%%%%%")

			if current_node.next_node.data == input1:
				prev1 = current_node
				targetNode1 = current_node.next_node

			if current_node.next_node.data == input2:
				prev2 =  current_node
				targetNode2 = current_node.next_node
			
			# increament the counter
			current_node = current_node.next_node

		# perform the swap

		if targetNode1 and targetNode2:
			print("############33")
			print(targetNode1.data)
			# handle scenario where one of the inouts is the head node
			# if not then make the previous node to the target node point to the other target node
			if prev1 == None:
				self.head = targetNode2
			else:
				prev1.next_node = targetNode2

			if prev2 == None:
				self.head = targetNode1
			else:
				prev2.next_node = targetNode1


			# then swap the target nodes using the all basic and known python swap
			targetNode1.next_node, targetNode2.next_node = targetNode2.next_node, targetNode1.next_node

		else:
			msg="one or both of the inputs is not in the linked list"
			return msg



	def reverseLinkedList(self):
		# Important items to look at 
		# 1. Prev node
		# 2. Current node
		# 3. Next node

		# First check if the linked list is empty
		if self.head is None:
			msg = "Cannot reverse an empty linked list"
			return msg

		current_node = self.head

		# Check if there's only one node in the linked list
		if current_node.next_node is None:
			msg = "Cannot reverse a linked list with only one node"
			return msg

		prev_node = None

		# If there's more than one node in the linked list, then we can reverse the linked list

		while current_node.next_node is not None:
			# Keep track of the prev_node and the current node's next node
			next_node = current_node.next_node

			current_node.next_node = prev_node

			# increment the prev and current node counters
			prev_node = current_node
			current_node = next_node

			# At the end of this iteration, the last node will still have it's next pointer in the default

		# make the last node the head 
		self.head = current_node
		current_node.next_node = prev_node

	def reversedLinkedListRecirsive(self):

		# check if the linked list is empty
		if self.head is None:
			msg="The linked list is empty, cannot reverse"
			return msg

		# check of there's only one node in the linked list
		current_node = self.head

		if current_node.next_node is None:
			msg="Cannot reverse a linked list with only one node"
			return msg

		prev = None

		# call our base case
		current_node, prev = self._reverseRecursive(current_node, prev)

		self.head = current_node
		current_node.next_node = prev

	def _reverseRecursive(self, current_node, prev):

		if current_node.next_node is None:
			return (current_node, prev)

		else:
			# capture the next node on a temp variable
			nxt  = current_node.next_node


			# point the current node's pointer to point the prev node
			current_node.next_node = prev

			# move the previous node pointer to the current node
			prev = current_node

			# move the current node pointer to point to the nxt node
			current_node = nxt

			# call this fucntion recursively
			return self._reverseRecursive(current_node, prev)















		

	

		




llist = LinkedList()
llist.appendNode(1)
llist.appendNode(2)
llist.appendNode(3)
llist.appendNode(4)
llist.appendNode(5)
llist.appendNode(6)
# print(llist.insertNode(4,1))
# print(llist.deleteNode(6))
# print(llist.delByIndex(5))
# print(llist.NodeSwap(1,2))
print(llist.reverseLinkedList())
# print(llist.nodeSwap_recap(12,12))
print(llist.printNodeData())




# print(llist.getLength())




# Doubly linked List


