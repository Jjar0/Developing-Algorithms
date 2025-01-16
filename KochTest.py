import unittest
from unittest.mock import patch, MagicMock
from Recursion import KochSnowflake  # Import the class here

class TestKochSnowflake(unittest.TestCase):
    def setUp(self):
        self.depth = 2
        self.side_length = 300
        with patch("turtle.Turtle") as MockTurtle, patch("turtle.Screen") as MockScreen:
            self.mock_turtle = MockTurtle.return_value
            self.mock_screen = MockScreen.return_value
            self.snowflake = KochSnowflake(self.depth, self.side_length)
            self.snowflake.t = self.mock_turtle
            self.snowflake.screen = self.mock_screen

    @patch("turtle.Turtle")
    def test_config(self, mock_turtle):
        self.snowflake.config()
        self.snowflake.screen.bgcolor.assert_called_once_with("white")
        self.snowflake.t.speed.assert_called_once_with(0)
        self.snowflake.t.penup.assert_called_once()
        self.snowflake.t.goto.assert_called_once_with(-self.side_length / 2, self.side_length / 3)
        self.snowflake.t.pendown.assert_called_once()
        self.snowflake.t.hideturtle.assert_called_once()

    @patch("turtle.Turtle")
    def test_draw_segment(self, mock_turtle):
        self.snowflake.t = mock_turtle.return_value

        # Test depth 0
        self.snowflake.drawSegment(300, 0)
        self.snowflake.t.forward.assert_called_once_with(300)

        # Test depth 1
        self.snowflake.t.reset_mock()
        self.snowflake.drawSegment(300, 1)
        expected_length = 300 / 3.0

        forward_calls = [call[0][0] for call in self.snowflake.t.forward.call_args_list]
        self.assertEqual(forward_calls, [expected_length] * 4)
        self.assertEqual(self.snowflake.t.left.call_count, 2)
        self.assertEqual(self.snowflake.t.right.call_count, 1)

    @patch("turtle.Turtle")
    def test_draw_snowflake(self, mock_turtle):
        self.snowflake.t = mock_turtle.return_value

        # Mock the drawSegment method to avoid recursion in this test
        self.snowflake.drawSegment = MagicMock()

        # Call the drawSnowflake method
        self.snowflake.drawSnowflake()

        # Ensure drawSegment is called three times with correct parameters
        self.assertEqual(self.snowflake.drawSegment.call_count, 3)
        expected_calls = [
            ((self.side_length, self.depth),),  # Call 1
            ((self.side_length, self.depth),),  # Call 2
            ((self.side_length, self.depth),),  # Call 3
        ]
        self.snowflake.drawSegment.assert_has_calls(expected_calls, any_order=False)

        # Check that the turtle turns right 120 degrees after each side
        self.assertEqual(self.snowflake.t.right.call_count, 3)
        self.snowflake.t.right.assert_any_call(120)

    @patch("turtle.Screen")
    @patch("turtle.Turtle")
    def test_run(self, mock_turtle, mock_screen):
        self.snowflake.t = mock_turtle.return_value
        self.snowflake.screen = mock_screen.return_value

        self.snowflake.config = MagicMock()
        self.snowflake.drawSnowflake = MagicMock()

        self.snowflake.run()
        self.snowflake.config.assert_called_once()
        self.snowflake.drawSnowflake.assert_called_once()
        self.snowflake.screen.mainloop.assert_called_once()


if __name__ == "__main__":
    unittest.main()