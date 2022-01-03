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
        self.world_size = (30, 30)
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
            # alignment_arrows.append(ax.plot([self.boids[i].r[0], self.boids[i].r[0] + np.cos(self.boids[i].alignment)],
            #                                 [self.boids[i].r[1], self.boids[i].r[1] + np.sin(self.boids[i].alignment)],
            #                                 lw=0.8, c='b')[0])
            # cohesion_arrows.append(ax.plot([self.boids[i].r[0], self.boids[i].r[0] + np.cos(self.boids[i].cohesion)],
            #                                [self.boids[i].r[1], self.boids[i].r[1] + np.sin(self.boids[i].cohesion)],
            #                                lw=0.8, c='g')[0])

        # changing the code here to just look at one boid
        # alignment_arrow = ax.plot([self.boids[0].r[0], self.boids[0].r[0] + np.cos(self.boids[0].alignment)],
        #                           [self.boids[0].r[1], self.boids[0].r[1] + np.sin(self.boids[0].alignment)],
        #                           lw=0.8, c='b')[0]
        # cohesion_arrow = ax.plot([self.boids[0].r[0], self.boids[0].r[0] + np.cos(self.boids[0].cohesion)],
        #                          [self.boids[0].r[1], self.boids[0].r[1] + np.sin(self.boids[0].cohesion)],
        #                          lw=0.8, c='g')[0]

        # create the range of visibility
        visible_zone = ax.add_patch(plt.Circle(self.boids[0].r,
                                               self.boids[0].visibility,
                                               fill=False))

        # plot the center of mass
        # cm = np.average(np.array([boid.r for boid in self.boids]), axis=0)
        # cm_point = ax.plot(*cm, c='g', marker='o', ms=20)[0]

        # a function used in mpl animation
        def animate(frame=True):
            """This function is necessary to do an mpl animation. The variable
            i is used to update the image."""

            # calc boid_0's visibility list
            visible_list = [boid for boid in self.boids if np.sqrt(np.sum((boid.r - self.boids[0].r)**2)) < self.boids[0].visibility]

            # calculate the new turn
            for j in range(len(self.boids)):
                self.boids[j].calculate_turn(self.boids)

            # update the boid
            for i, boid in enumerate(self.boids):
                boid.update_position(self.delta_t)

                # now check the boundaries
                self.check_boundaries(boid)

                # now update the point on the plot
                points[i].set_xdata(boid.r[0])
                points[i].set_ydata(boid.r[1])
                if boid in visible_list:
                    points[i].set_color('r')
                else:
                    points[i].set_color('k')

            # update the cohesion arrow
            # alignment_arrow.set_xdata([self.boids[0].r[0],
            #                            self.boids[0].r[0] + np.cos(self.boids[0].alignment)])
            # alignment_arrow.set_ydata([self.boids[0].r[1],
            #                            self.boids[0].r[1] + np.sin(self.boids[0].alignment)])

            # # update the cohesion arrow
            # cohesion_arrow.set_xdata([self.boids[0].r[0],
            #                           self.boids[0].r[0] + np.cos(self.boids[0].cohesion)])
            # cohesion_arrow.set_ydata([self.boids[0].r[1],
            #                           self.boids[0].r[1] + np.sin(self.boids[0].cohesion)])

            # update the circle
            visible_zone.center = self.boids[0].r

            # plot the cm
            # cm = np.average(np.array([boid.r for boid in self.boids]), axis=0)
            # cm_point.set_xdata(cm[0])
            # cm_point.set_ydata(cm[1])
            return

        # this controls the animation
        # all integers are in ms (I believe)
        # ani = animation.FuncAnimation(fig, animate, frames=self.n_timesteps,
        #                               interval=40)

        # and finally, save the animation as a .gif
        # ani.save(self.world_name + '.gif')
        
        # this is the option for a non-.gif animation
        while True:
            #plt.show()
            plt.pause(0.001)
            animate()
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
