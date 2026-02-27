from linked_lists.circular_linked_list import CircularLinkedList, CircularNode

def test_linked_test_creation():
    node: CircularNode = CircularNode(10)

    assert node.data == 10
    assert node.next is None

    cll:CircularLinkedList = CircularLinkedList()
    assert cll.head is None
    assert cll.length == 0