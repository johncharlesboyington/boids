import numpy as np


class Boid():
    """Boid Object"""

    def __init__(self, r_initial, v_initial, theta_initial):
        self.r = r_initial  # numpy array (x, y)
        self.v = v_initial  # float
        self.theta = theta_initial  # float
        self.initialize_turn()
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

    def set_theta(self, theta):
        """blah"""
        self.theta = theta

    def initialize_turn(self):
        """blah"""
        # cohesion
        self.cohesion = 0

    def calculate_turn(self, boids):
        """blah"""
        # cohesion
        v = 0.2
        self.cohesion = (v * self.calc_cohesion(boids)) + self.theta
        self.set_theta(self.cohesion)
        return

    def calc_separation(self):
        """blah"""
        return

    def calc_alignment(self):
        """blah"""
        return

    def calc_cohesion(self, boids):
        """blah"""
        # calculate the relevent center of mass
        boid_cm = np.average(np.array([boid.r for boid in boids]), axis=0)

        # calculate the angle between the two points
        new_vector = self.r - boid_cm
        if new_vector[0]:
            if new_vector[1] >= 0:
                new_theta = np.arctan(new_vector[1] / new_vector[0])
            elif new_vector[1] < 0:
                new_theta = - np.arctan(new_vector[1] / new_vector[0])
        else:
            new_theta = self.theta
        return new_theta - self.theta
