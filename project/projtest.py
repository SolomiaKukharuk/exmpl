import unittest
from modulepro import _Coordinates, Draw
import numpy as np


class TestCoordinates(unittest.TestCase):

    def test_trajectory_calculation(self):
        # Test trajectory calculation for a specific set of inputs
        roll, pitch, yaw = 10, 20, 30
        initial_position = (0, 0, 100)
        coords = _Coordinates(roll, pitch, yaw, initial_position)
        trajectory = coords._trajectory()
        # Assert that the trajectory is not empty
        self.assertTrue(len(trajectory) > 0)
        # Assert that the trajectory contains the initial position
        self.assertTrue((trajectory[0] == np.array(initial_position)).all())

    def test_trajectory_draw(self):
        # Test trajectory drawing functionality
        roll, pitch, yaw = 10, 20, 30
        initial_position = (0, 0, 100)
        draw = Draw(roll, pitch, yaw, initial_position)
        # Mock user input for canvas properties
        draw.get_canvas_properties = lambda: (800, 600, "white")
        # Check if draw_trajectory method runs without errors
        draw.draw_trajectory()
        # Add more specific assertions if possible


if __name__ == '__main__':
    unittest.main()
