import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from boid import Boid


class World():
    """World Object."""

    def __init__(self):
        """blah"""
        # hardcoding all values for now
        # world parameters
        self.world_name = 'random_boids'
        self.world_size = (10, 10)
        self.delta_t = 0.5
        self.n_timesteps = 100
        self.initial_boid_r = np.array([0, 0])
        self.initial_boid_v = 1
        # self.initial_boid_theta = -2
        self.boids = []
        self.N_boids = 100

        # create the boids (initially will just be one)
        # for _ in range(self.N_boids):
        #     self.boids.append(Boid(self.initial_boid_r,
        #                            self.initial_boid_v,
        #                            self.initial_boid_theta))
        for _ in range(self.N_boids):
            self.boids.append(Boid(self.initial_boid_r,
                                   self.initial_boid_v,
                                   rand() * 2 * np.pi))

        # initialize the environment
        fig = plt.figure(0, figsize=(30, 30))
        ax = fig.add_subplot(111)
        ax.set_xlim(-self.world_size[0] / 2, self.world_size[0] / 2)
        ax.set_ylim(-self.world_size[1] / 2, self.world_size[1] / 2)

        # initialize the boids (one in this case)
        # this is the endpoint
        points = []
        for i in range(self.N_boids):
            points.append(ax.plot(*self.boids[i].r, c='k',
                                  marker='o', ms=10)[0])

        # a function used in mpl animation
        def animate(i):
            """This function is necessary to do an mpl animation. The variable
            i is used to update the image."""

            # update the boid
            for i, boid in enumerate(self.boids):
                boid.update_position(self.delta_t)

                # now check the boundaries
                self.check_boundaries(boid)

                # now update the point on the plot
                points[i].set_xdata(boid.r[0])
                points[i].set_ydata(boid.r[1])
            return

        # this controls the animation
        # all integers are in ms (I believe)
        ani = animation.FuncAnimation(fig, animate, frames=self.n_timesteps,
                                      interval=40)

        # and finally, save the animation as a .gif
        ani.save(self.world_name + '.gif')
        return

    def check_boundaries(self, boid):
        """blah"""
        # check the x
        if boid.r[0] > self.world_size[0] / 2:
            boid.set_x(boid.r[0] - self.world_size[0])
        elif boid.r[0] < -self.world_size[0] / 2:
            boid.set_x(boid.r[0] + self.world_size[0])

        # check the y
        if boid.r[1] > self.world_size[1] / 2:
            boid.set_y(boid.r[1] - self.world_size[1])
        elif boid.r[1] < -self.world_size[1] / 2:
            boid.set_y(boid.r[1] + self.world_size[1])
        return


if __name__ == '__main__':
    World()
