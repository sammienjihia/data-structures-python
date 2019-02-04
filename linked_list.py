"""
This is an implementation of a singly linked list in python
"""

# Create a class node with the data and next pointer variables

class Node:

	def __init__(self, data):

		self.data = data
		self.next_node = None 

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

	def deleteNode(self, targetNodeData):
		# Scenario 1: Linked lis is empty
		# scenario 2: Target Node not in the linked list

		if self.head is None:
			msg = "Linked List is empty"
			return msg

		current_node = self.head

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

		




llist = LinkedList()
llist.appendNode(1)
llist.appendNode(2)
llist.appendNode(3)
llist.appendNode(4)
llist.appendNode(5)
llist.appendNode(6)
print(llist.insertNode(7,4))
print(llist.deleteNode(2))
print(llist.printNodeData())

