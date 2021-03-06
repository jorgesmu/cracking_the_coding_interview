from linked_list import Node

# Time: O(n)
def floyd(li):
	if not li:
		return False
	slow = li
	fast = li.next
	while fast and fast.next and fast.next.next:
		if slow == fast:
			return True
		slow = slow.next
		fast = fast.next.next
	return False

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n4.next = n2
# print('cycled for cycled list: ', cycled_list(n1))
print('cycled(floyd)for cycled list: ', floyd(n1))


n6 = Node(5)
n5 = Node(3, n6)
n4.next = n5
# print('cycled for non cycled list: ', cycled_list(n1))
print('cycled(floyd) for non cycled list: ', floyd(n1))