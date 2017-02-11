from LinkedList import LinkedList
from LinkedList import LinkedListNode

def partition(llist, partition):
	if llist.head is None:
		return

	current = llist.head
	leftTail = LinkedListNode(None, current)

	while current.value < partition:
		leftTail = leftTail.next
		current = current.next

	current = leftTail
	firstTime = True
	while current.next:
		if current.next.value >= partition:
			current = current.next
		else:
			if firstTime and leftTail.value:
				llist.head = leftTail
				firstTime = False
			temp = leftTail.next
			leftTail.next = current.next
			leftTail = current.next
			current.next = leftTail.next
			leftTail.next = temp

	print llist

def partition_v2(llist, partition):
	right = LinkedList()
	left = LinkedList()
	for x in llist:
		if x.value < partition:
			right.add(x.value)
		elif x.value >= partition:
			left.add(x.value)
	right.tail.next = left.head
	print right

def main():

	ll = LinkedList()
	ll.add_multiple([3,5,8,5,10,2,1])
	print ll
	partition_v2(ll, 5)

	ll = LinkedList()
	ll.add_multiple([9,8,7,6,5,4,3])
	print ll
	partition_v2(ll, 5)

if __name__ == '__main__':
	main()