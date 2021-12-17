import numpy as np


class Boid():
    """Boid Object"""

    def __init__(self, r_initial, v_initial, theta_initial):
        self.r = r_initial  # numpy array (x, y)
        self.v = v_initial  # float
        self.theta = theta_initial  # float
        return

    def update_position(self, delta_t):
        """blah"""
        delta_x = self.v * delta_t * np.cos(self.theta)
        delta_y = self.v * delta_t * np.sin(self.theta)
        self.r = self.r + np.array([delta_x, delta_y])
        return

    def set_x(self, x):
        """blah"""
        self.r[0] = x

    def set_y(self, y):
        """blah"""
        self.r[1] = y
