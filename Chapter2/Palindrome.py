from LinkedList import LinkedList

def isPalindrome(ll):
	slow = ll.head
	fast = ll.head

	stack = []
	counter = 0
	while fast and fast.next:
		#print fast.value
		counter += 1
		stack.append(slow.value)
		slow = slow.next
		fast = fast.next.next

	print stack

	if counter%2==0:
		slow = slow.next

	while slow:
		if slow.value != stack.pop():
			return False
		slow = slow.next
	return True



def main():
	ll = LinkedList()
	ll.add_multiple(['a','b','c','b','a'])
	print isPalindrome(ll)

	ll = LinkedList()
	ll.add_multiple(['a','b','c','c','b','a'])
	print isPalindrome(ll)

	ll = LinkedList()
	ll.add_multiple(['x','b','c','c','a'])
	print isPalindrome(ll)

if __name__ == '__main__':
	main()