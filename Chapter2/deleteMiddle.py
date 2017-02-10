from LinkedList import LinkedList

def deleteMiddle(node):
	node.value = node.next.value
	node.next = node.next.next

def main():
	ll = LinkedList([1,2,3])
	middleNode = ll.add(4)
	ll.add_multiple([5,6,7])
	print ll

	deleteMiddle(middleNode)
	print ll

if __name__ == '__main__':
	main()