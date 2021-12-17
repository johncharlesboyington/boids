import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from boid import Boid


class World():
    """World Object."""

    def __init__(self):
        """blah"""
        # hardcoding all values for now
        # world parameters
        self.world_name = 'single_boid'
        self.world_size = (10, 10)
        self.delta_t = 0.05
        self.n_timesteps = 100
        self.initial_boid_r = np.array([0, 0])
        self.initial_boid_v = 1
        self.initial_boid_theta = 0
        self.boids = []
        self.N_boids = 1

        # create the boids (initially will just be one)
        for _ in range(self.N_boids):
            self.boids.append(Boid(self.initial_boid_r,
                                   self.initial_boid_v,
                                   self.initial_boid_theta))

        # initialize the environment
        fig = plt.figure(0, figsize=(30, 30))
        ax = fig.add_subplot(111)
        ax.set_xlim(-self.world_size[0] / 2, self.world_size[0] / 2)
        ax.set_ylim(-self.world_size[1] / 2, self.world_size[1] / 2)

        # initialize the boids (one in this case)
        # this is the endpoint
        point = ax.plot(*self.boids[0].r, c='k', marker='o', ms=5)[0]

        # a function used in mpl animation
        def animate(i):
            """This function is necessary to do an mpl animation. The variable
            i is used to update the image."""

            # update the boid
            self.boids[0].update_position(self.delta_t)

            # now update the point on the plot
            point.set_xdata(self.boids[0].r[0])
            point.set_ydata(self.boids[0].r[1])
            return

        # this controls the animation
        # all integers are in ms (I believe)
        ani = animation.FuncAnimation(fig, animate, frames=self.n_timesteps,
                                      interval=50)

        # and finally, save the animation as a .gif
        ani.save(self.world_name + '.gif')
        return


if __name__ == '__main__':
    World()
