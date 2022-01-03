import numpy as np


class Boid():
    """Boid Object"""

    def __init__(self, r_initial, v_initial):
        # hardcoded boid parameters
        self.visibility = 5
        self.collision_radius = 0.5
        self.field_of_view = 90 * (np.pi / 180)
        self.max_v = 0.5

        # boid parameters
        self.r = r_initial  # numpy array (x, y)
        self.v = v_initial  # numpy array (x, y)
        self.initialize_turn()
        return

    def update_position(self, delta_t):
        """blah"""
        # check against maximum velocity and scale
        if np.linalg.norm(self.v) > self.max_v:
            self.v *= (self.max_v / np.linalg.norm(self.v))

        # update
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
        self.margin = np.array([0, 0])

    def calculate_turn(self, boids, world_size, margin):
        """blah"""
        # calculate visible boids
        visible_boids = [boid for boid in boids
                         if (np.sqrt(np.sum((boid.r - self.r)**2)) < self.visibility
                             and calc_angle((boid.r - self.r), self.v) < self.field_of_view
                             and id(self) != id(boid))]
        colliding_boids = [boid for boid in boids
                           if (np.sqrt(np.sum((boid.r - self.r)**2)) < self.collision_radius
                               and calc_angle((boid.r - self.r), self.v) < self.field_of_view
                               and id(self) != id(boid))]

        # separation
        self.separation = self.calc_separation(colliding_boids)

        # alignment
        self.alignment = self.calc_alignment(visible_boids)

        # cohesion
        self.cohesion = self.calc_cohesion(visible_boids)

        # margin
        self.margin = self.calc_margin(world_size, margin)

        # weighted summed turning
        self.v = self.separation + self.alignment + self.cohesion + self.margin + self.v
        return

    def calc_separation(self, boids):
        """blah"""
        return 0.05 * np.sum(np.array([-(boid.r - self.r) for boid in boids]), axis=0)

    def calc_alignment(self, boids):
        """blah"""
        # calculate the average direction
        if boids:
            boid_v = np.average(np.array([boid.v for boid in boids]), axis=0)
        else:
            boid_v = self.v

        # subtract
        return 0.05 * (boid_v - self.v)

    def calc_cohesion(self, boids):
        """blah"""
        # calculate the relevent center of mass
        if boids:
            boid_cm = np.average(np.array([boid.r for boid in boids]), axis=0)
        else:
            boid_cm = self.r

        # calculate the angle between the two points
        return 0.005 * (boid_cm - self.r)

    def calc_margin(self, world_size, margin):
        """blah"""
        # calculate which direction to move
        dimension = np.array(abs(self.r) > ((world_size / 2) - margin)).astype(int)
        direction = - np.array(self.r / abs(self.r)).astype(int)
        return 0.1 * dimension * direction


def calc_angle(u, v):
    """calculates the angle between two vectors"""
    top = np.sum(u * v)
    bot = np.sqrt(np.sum(u**2)) + np.sqrt(np.sum(v**2))
    return np.arccos(top / bot)
