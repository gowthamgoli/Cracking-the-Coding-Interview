from LinkedList import LinkedList

def sumLists_reverse(l1,l2):
	carry = 0
	curr_l1 = l1.head
	curr_l2 = l2.head
	output = LinkedList()

	while curr_l1 and curr_l2:
		a = curr_l1.value
		b = curr_l2.value
		s = a + b + carry
		carry = s/10
		output.add(s%10)
		curr_l1 = curr_l1.next
		curr_l2 = curr_l2.next

	if curr_l1 is None and curr_l2 is None:
		return output

	if curr_l1 is None:
		while curr_l2:
			s = curr_l2.value + carry
			carry = s/10
			output.add(s%10)
			curr_l2 = curr_l2.next
		if carry!=0:
			output.add(carry)

	if curr_l2 is None:
		while curr_l1:
			s = curr_l1.value + carry
			carry = s/10
			output.add(s%10)
			curr_l1 = curr_l1.next
		if carry!=0:
			output.add(carry)

	return output


def main():
	list1 = LinkedList([7,1,6,9])
	list2 = LinkedList([5,9,6])
	print sumLists_reverse(list1,list2)

if __name__ == '__main__':
	main()