#Assignment 3
from as3_tree import Tree
arr = []
class Result:
	def __init__(self, sol=[], val=-1000):
			self.solution = sol
			self.value = val
			
class MNX:
	def __init__(self, data_list):
		self.tree = Tree()	
		self.tree.init_tree(data_list)
		self.root = self.tree.root
		self.currentNode = None
		self.successors = []		
		return
        
	def terminalTest(self, node):
		assert node is not None
		return len(node.children) == 0

	def utilityChecking(self, node):
		assert node is not None
		return node.value

	def getChildren(self, node):
		assert node is not None
		return node.children

	def traversed(self, node, terminal_val):
		global arr
		for i in self.getChildren(node):
			if i.value == terminal_val:
				arr.append(i.Name)
				self.traversed(i, terminal_val)
				break

	def minimax(self):
		global arr
		terminal_val = self.max_v(self.root)
		successors = self.getChildren(self.root)
		res=Result();
		arr.append(self.root.Name)
		self.traversed(self.root, terminal_val)
#################  Return the solution here  #################
		res.value=terminal_val #you put the best terminal value for root node here
		res.solution=arr #you put the solution_array here
#################  Return the solution here  #################
		return res


	def max_v(self, node):
		if self.terminalTest(node):
			return self.utilityChecking(node)		
		max_v = -1000 #we use 1000 as the initial_maximum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			max_v = max(max_v, self.min_v(deeper_node))
		node.value = max_v
		return max_v

	def min_v(self, node):
		if self.terminalTest(node):
			return self.utilityChecking(node)
		min_v = 1000 #we use -1000 as the initial_minimum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			min_v = min(min_v, self.max_v(deeper_node))
		node.value = min_v
		return min_v