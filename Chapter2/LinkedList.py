from random import randint

class LinkedListNode():
	def __init__(self, value, nextNode = None, prevNode = None):
		self.value = value
		self.next = nextNode
		self.prev = prevNode

	def __str__(self):
		print str(self.value)

class LinkedList():
	def __init__(self, values=None):
		self.head = None
		self.tail = None
		if values:
			self.add_multiple(values)

	def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.next

	def __str__(self):
		values = [str(x.value) for x in self]
		return " -> ".join(values)

	def __len__(self):
		result = 0
		node = self.head
		while node:
			result += 1
			node = node.next
		return result

	def add(self, value):
		if self.head is None:
			self.head = self.tail = LinkedListNode(value)
		else:
			self.tail.next = LinkedListNode(value)
			self.tail = self.tail.next
		return self.tail

	def add_to_beginning(self, value):
		if self.head is None:
			self.head = self.tail = LinkedListNode(vale)
		else:
			self.head = LinkedListNode(value, self.head)

	def add_multiple(self, values):
		for v in values:
			self.add(v)

	def generate(self, n, min_value, max_value):
		#self.head = self.tail = None
		for i in range(n):
			self.add(randint(min_value, max_value))
		return self