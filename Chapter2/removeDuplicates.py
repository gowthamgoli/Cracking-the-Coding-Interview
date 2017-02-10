from LinkedList import LinkedList
from collections import defaultdict

def removeDups_v1(llist):
	current = llist.head
	visited = set([current.value])
	while current.next:
		if current.next.value in visited:
			current.next = current.next.next
		else:
			visited.add(current.next.value)
			current = current.next

	#print llist


def main():
	ll = LinkedList()
	ll.generate(100,0,9)
	#print ll
	removeDups_v1(ll)
	print ll

if __name__ == '__main__':
	main()