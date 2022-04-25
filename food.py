import numpy as np
from numpy.random import rand


class Food():
    """Food Object"""

    def __init__(self, r):
        # hardcoded food parameters
        self.r = r
        self.value = 100
        self.max_value = 100
        self.eating_radius = 1
        self.alive = True
        return

    def can_eat(self, consumer_r):
        """blah"""
        d = np.sqrt(np.sum((consumer_r - self.r)**2))
        if d <= self.eating_radius:
            return True
        else:
            return False

    def eat(self, value_eaten):
        """blah"""
        self.value -= value_eaten
        if self.value <= 0:
            self.alive = False
        return

    def grow(self, value_grown):
        """blah"""
        self.value += value_grown
        if self.value >= self.max_value:
            self.value = self.max_value
        return


def create_foods(N_foods, world_size):
    """blah"""
    # some starting values
    foods = []

    # create the boids (initially will just be one)
    for _ in range(N_foods):
        foods.append(Food(np.array([rand() * world_size[0] - (world_size[0] / 2),
                                    rand() * world_size[0] - (world_size[0] / 2)])))

    return foods
