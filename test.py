import unittest
from io import StringIO
import sys
from LinkedList import Node, LinkedList  # Assuming your code is in a file named linked_list_module.py

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linkedList = LinkedList()

    def test_push(self):
        self.linkedList.push(10)
        self.linkedList.push(20)
        self.assertEqual(self.linkedList.head.data, 20)
        self.assertEqual(self.linkedList.head.next.data, 10)

    def test_pop(self):
        self.linkedList.push(10)
        self.linkedList.push(20)
        popped_value = self.linkedList.pop()
        self.assertEqual(popped_value, 20)
        self.assertEqual(self.linkedList.head.data, 10)

        # Test pop on empty list
        self.linkedList.pop()
        popped_value = self.linkedList.pop()
        self.assertIsNone(popped_value)

    def test_reverse(self):
        self.linkedList.push(10)
        self.linkedList.push(20)
        self.linkedList.push(30)
        self.linkedList.reverse()

        self.assertEqual(self.linkedList.head.data, 10)
        self.assertEqual(self.linkedList.head.next.data, 20)
        self.assertEqual(self.linkedList.head.next.next.data, 30)

    def test_sort(self):
        self.linkedList.push(30)
        self.linkedList.push(10)
        self.linkedList.push(20)
        self.linkedList.sort()

        self.assertEqual(self.linkedList.head.data, 10)
        self.assertEqual(self.linkedList.head.next.data, 20)
        self.assertEqual(self.linkedList.head.next.next.data, 30)

    def test_display_empty_list(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.linkedList.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "List is empty.")

    def test_display_non_empty_list(self):
        self.linkedList.push(10)
        self.linkedList.push(20)
        captured_output = StringIO()
        sys.stdout = captured_output
        self.linkedList.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "20 > 10")


unittest.main(verbosity=2)
