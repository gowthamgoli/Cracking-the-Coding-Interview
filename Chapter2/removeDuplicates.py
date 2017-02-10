from LinkedList import LinkedList
from collections import defaultdict

def removeDups_v1(llist):
	current = llist.head
	if current is None:
		return
	visited = set([current.value])
	while current.next:
		if current.next.value in visited:
			current.next = current.next.next
		else:
			visited.add(current.next.value)
			current = current.next

	#print llist

def removeDups_v2(llist):
	current = llist.head
	if current is None:
		return
	while current:
		slider = current
		while slider.next:
			if slider.next.value == current.value:
				slider.next = slider.next.next
			else:
				slider = slider.next
		current = current.next


def main():
	ll = LinkedList()
	ll.generate(100,0,9)
	#print ll
	removeDups_v1(ll)
	print ll

	ll = LinkedList()
	ll.generate(100,0,9)
	#print ll
	removeDups_v1(ll)
	print ll

if __name__ == '__main__':
	main()