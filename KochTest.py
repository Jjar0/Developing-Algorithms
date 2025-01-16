import unittest
from unittest.mock import MagicMock, patch
from koch_snowflake import KochSnowflake  # Assuming the class is in a file named `koch_snowflake.py`

class TestKochSnowflake(unittest.TestCase):
    def setUp(self):
        self.depth = 2
        self.side_length = 300
        self.snowflake = KochSnowflake(self.depth, self.side_length)

    @patch("turtle.Turtle")
    def test_config(self, mock_turtle):
        mock_screen = MagicMock()
        self.snowflake.screen = mock_screen
        
        self.snowflake.config()
        
        mock_screen.bgcolor.assert_called_once_with("white")
        self.snowflake.t.speed.assert_called_once_with(0)
        self.snowflake.t.penup.assert_called_once()
        self.snowflake.t.goto.assert_called_once_with(-self.side_length / 2, self.side_length / 3)
        self.snowflake.t.pendown.assert_called_once()
        self.snowflake.t.hideturtle.assert_called_once()

    @patch("turtle.Turtle")
    def test_draw_segment(self, mock_turtle):
        self.snowflake.t = mock_turtle.return_value

        # Test depth 0
        self.snowflake.drawSegment(100, 0)
        self.snowflake.t.forward.assert_called_once_with(100)

        # Test depth 1
        self.snowflake.t.reset_mock()
        self.snowflake.drawSegment(300, 1)

        # The segment length should be divided into thirds
        expected_length = 300 / 3.0
        self.assertEqual(self.snowflake.t.forward.call_count, 1)
        self.assertEqual(self.snowflake.t.left.call_count, 2)
        self.assertEqual(self.snowflake.t.right.call_count, 1)

    @patch("turtle.Turtle")
    def test_draw_snowflake(self, mock_turtle):
        self.snowflake.t = mock_turtle.return_value
        self.snowflake.drawSnowflake()

        # Three sides should be drawn, turning 120 degrees after each
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