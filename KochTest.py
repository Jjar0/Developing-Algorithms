import unittest
from unittest.mock import MagicMock
from Recursion import KochSnowflake  # Assuming the class is in koch_snowflake.py

class TestKochSnowflake(unittest.TestCase):

    def setUp(self):
        self.depth = 4
        self.side_length = 400
        self.snowflake = KochSnowflake(depth=self.depth, side_length=self.side_length)
        self.snowflake.t = MagicMock()  # Mock the turtle object to avoid actual drawing

    def test_initialization(self):
        self.assertEqual(self.snowflake.depth, self.depth)
        self.assertEqual(self.snowflake.side_length, self.side_length)
        self.assertIsNotNone(self.snowflake.t)
        self.assertIsNotNone(self.snowflake.screen)

    def test_config(self):
        self.snowflake.config()
        self.snowflake.t.speed.assert_called_with(0)
        self.snowflake.t.penup.assert_called_once()
        self.snowflake.t.goto.assert_called_once_with(-self.side_length / 2, self.side_length / 3)
        self.snowflake.t.pendown.assert_called_once()
        self.snowflake.t.hideturtle.assert_called_once()

    def test_drawSegment_depth_zero(self):
        length = 100
        self.snowflake.drawSegment(length, 0)
        self.snowflake.t.forward.assert_called_once_with(length)

    def test_drawSegment_recursive_call(self):
        length = 300
        depth = 2
        self.snowflake.drawSegment(length, depth)
        self.assertEqual(self.snowflake.t.forward.call_count, 0)  # Should not call forward directly
        # Check the recursive calls (mocked, so no real recursion occurs)
        expected_calls = [
            unittest.mock.call(length / 3),
            unittest.mock.call(length / 3),
            unittest.mock.call(length / 3),
            unittest.mock.call(length / 3),
        ]
        self.assertEqual(self.snowflake.t.forward.call_args_list, [])

    def test_drawSnowflake(self):
        self.snowflake.drawSnowflake()
        self.assertEqual(self.snowflake.t.right.call_count, 3)
        self.snowflake.t.right.assert_any_call(120)

    def test_run(self):
        self.snowflake.config = MagicMock()
        self.snowflake.drawSnowflake = MagicMock()
        self.snowflake.screen.mainloop = MagicMock()

        self.snowflake.run()
        self.snowflake.config.assert_called_once()
        self.snowflake.drawSnowflake.assert_called_once()
        self.snowflake.screen.mainloop.assert_called_once()

unittest.main()