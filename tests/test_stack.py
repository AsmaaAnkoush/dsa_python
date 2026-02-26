import pytest
from stacks.stack import Stack , Node

def test_stack_node_creation():
    node: Node = Node(10)

    assert node.value == 10
    assert node.next is None

    stack: Stack = Stack()
    assert stack.top is None
    assert stack.length == 0