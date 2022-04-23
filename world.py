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
        self.world_name = 'boids'
        self.world_size = np.array([30, 30])
        self.margin = 1
        self.delta_t = 1.0
        self.n_timesteps = 500
        self.initial_boid_r = np.array([0, 0])
        self.boids = []
        self.N_boids = 10

        # create the boids (initially will just be one)
        for _ in range(self.N_boids):
            self.boids.append(Boid(np.array([rand() * self.world_size[0] - (self.world_size[0] / 2),
                                             rand() * self.world_size[0] - (self.world_size[0] / 2)]),
                                   np.array([2 * rand() - 1, 2 * rand() - 1])))

        # initialize the environment
        fig = plt.figure(0, figsize=(30, 30))
        ax = fig.add_subplot(111)
        ax.set_xlim(-self.world_size[0] / 2, self.world_size[0] / 2)
        ax.set_ylim(-self.world_size[1] / 2, self.world_size[1] / 2)

        # initialize the boids
        points = []
        for i in range(self.N_boids):
            points.append(ax.plot(*self.boids[i].r, c='k',
                                  marker='o', ms=10)[0])

        # create the range of visibility
        visible_zone = ax.add_patch(plt.Circle(self.boids[0].r,
                                               self.boids[0].visibility,
                                               fill=False))

        # a function used in mpl animation
        def animate(frame=True):
            """This function is necessary to do an mpl animation. The variable
            i is used to update the image."""

            # calc boid_0's visibility list
            visible_list = [boid for boid in self.boids if np.sqrt(np.sum((boid.r - self.boids[0].r)**2)) < self.boids[0].visibility]

            # calculate the new turn
            for j in range(len(self.boids)):
                self.boids[j].calculate_turn(self.boids, self.world_size,
                                             self.margin)

            # list of dead boids
            dead_boids = []

            # update the boid
            for i, boid in enumerate(self.boids):

                if boid.alive:
                    boid.update_position(self.delta_t)
                    boid.calc_energy_loss()
                    boid.check_alive()

                # remove dead boids
                if not boid.alive:
                    dead_boids.append(i)

                # now update the point on the plot
                points[i].set_xdata(boid.r[0])
                points[i].set_ydata(boid.r[1])
                if boid in visible_list:
                    points[i].set_color('r')
                else:
                    points[i].set_color('k')

            # remove dead boids
            for i in dead_boids:
                self.boids.remove(self.boids[i])
                points[i].remove()
                points.remove(points[i])

            # stop the animation if all the boids are dead
            if len(self.boids) == 0:
                return False

            # update the circle
            visible_zone.center = self.boids[0].r
            return True

        # this controls the animation
        # all integers are in ms (I believe)
        # ani = animation.FuncAnimation(fig, animate, frames=self.n_timesteps,
        #                               interval=40)

        # and finally, save the animation as a .gif
        # ani.save(self.world_name + '.gif')

        # this is the option for a non-.gif animation
        run = True
        while run:
            plt.pause(0.001)
            run = animate()
        plt.close()
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
