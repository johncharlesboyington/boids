import numpy as np


class Boid():
    """Boid Object"""

    def __init__(self, r_initial, v_initial):
        # hardcoded boid parameters
        self.visibility = 5
        self.collision_zone = 0.5

        # boid parameters
        self.r = r_initial  # numpy array (x, y)
        self.v = v_initial  # numpy array (x, y)
        self.initialize_turn()
        return

    def update_position(self, delta_t):
        """blah"""
        self.r = self.r + (self.v * delta_t)
        return

    def set_x(self, x):
        """blah"""
        self.r[0] = x

    def set_y(self, y):
        """blah"""
        self.r[1] = y

    def initialize_turn(self):
        """blah"""
        self.separation = np.array([0, 0])
        self.alignment = np.array([0, 0])
        self.cohesion = np.array([0, 0])

    def calculate_turn(self, boids):
        """blah"""
        # calculate visible boids
        visible_boids = [boid for boid in boids if np.sqrt(np.sum((boid.r - self.r)**2)) < self.visibility and id(self) != id(boid)]
        colliding_boids = [boid for boid in boids if np.sqrt(np.sum((boid.r - self.r)**2)) < self.collision_zone and id(self) != id(boid)]

        # separation
        self.separation = self.calc_separation(colliding_boids)

        # alignment
        self.alignment = self.calc_alignment(visible_boids)

        # cohesion
        self.cohesion = self.calc_cohesion(visible_boids)

        # weighted summed turning
        self.v = self.separation + self.alignment + self.cohesion + self.v
        return

    def calc_separation(self, boids):
        """blah"""
        return 1.0 * np.sum(np.array([-(boid.r - self.r) for boid in boids]), axis=0)

    def calc_alignment(self, boids):
        """blah"""
        # calculate the average direction
        if boids:
            boid_v = np.average(np.array([boid.v for boid in boids]), axis=0)
        else:
            boid_v = self.v

        # subtract
        return 0.125 * (boid_v - self.v)

    def calc_cohesion(self, boids):
        """blah"""
        # calculate the relevent center of mass
        if boids:
            boid_cm = np.average(np.array([boid.r for boid in boids]), axis=0)
        else:
            boid_cm = self.r

        # calculate the angle between the two points
        return 0.01 * (boid_cm - self.r)
