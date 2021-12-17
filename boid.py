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
        self.r *= self.v * delta_t * np.array(np.cos(self.theta),
                                              np.sin(self.theta))
        return
