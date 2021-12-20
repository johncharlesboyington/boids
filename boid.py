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
        self.separation = 0
        self.alignment = 0
        self.cohesion = 0

    def calculate_turn(self, boids):
        """blah"""
        # alignment
        u = 0
        self.alignment = (u * self.calc_alignment(boids)) + self.theta

        # cohesion
        v = 1
        self.cohesion = (v * self.calc_cohesion(boids)) + self.theta
        self.set_theta(self.alignment + self.cohesion - self.theta)
        return

    def calc_separation(self):
        """blah"""
        return

    def calc_alignment(self, boids):
        """blah"""
        # calculate the average direction
        boid_theta = np.average(np.array([boid.theta for boid in boids]))

        return boid_theta - self.theta

    def calc_cohesion(self, boids):
        """blah"""
        # calculate the relevent center of mass
        boid_cm = np.average(np.array([boid.r for boid in boids]), axis=0)

        # calculate the angle between the two points
        new_vector = boid_cm - self.r
        if new_vector[0]:
            if new_vector[1] >= 0:
                new_theta = np.arctan(new_vector[1] / new_vector[0])
            elif new_vector[1] < 0:
                # new_theta = - np.arctan(new_vector[1] / new_vector[0])
                new_theta = np.arctan(new_vector[1] / new_vector[0])
        else:
            new_theta = self.theta
        return new_theta - self.theta
