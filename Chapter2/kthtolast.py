from LinkedList import LinkedList
def kthlast(ll,k):
	length = len(ll)
	fromFirst = length - k
	current = ll.head
	for i in range(fromFirst):
		current = current.next
	return current.value

def main():
	ll = LinkedList()
	ll.generate(10,0,9)
	print ll
	print kthlast(ll,10)

if __name__ == '__main__':
	main()