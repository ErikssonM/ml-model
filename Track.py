import numpy as np

class Track:

    #TODO: Create fitness function (field?) for track
    #TODO: Timetracking?

    def __init__(self, cars):
        self.obstacles = []
        self.load_default_track()

        self.cars = cars

    #TODO: Extend, import
    def load_default_track(self):
        self.obstacles.append(Obstacle([(300, 390), (500, 390), (500, 410), (300, 410)]))

    #Should work now?
    #https://stackoverflow.com/questions/563198/whats-the-most-efficent-way-to-calculate-where-two-line-segments-intersect
    def detect_collision(self):
        for car in self.cars:
            coords = car.get_car_boundaries()
            coords.append(coords[0])
            for i in range(len(coords) - 1):
                x1 = coords[i][0]
                y1 = coords[i][1]
                x2 = coords[i + 1][0] - x1
                y2 = coords[i + 1][1] - y1
                for obs in self.obstacles:
                    obs_coords = obs.points[:]
                    obs_coords.append(obs_coords[0])
                    for j in range(len(obs_coords) - 1):
                        ox1 = obs_coords[j][0]
                        oy1 = obs_coords[j][1]
                        ox2 = obs_coords[j + 1][0] - ox1
                        oy2 = obs_coords[j + 1][1] - oy1

                        #rxs
                        div = x2 * oy2 - y2 * ox2

                        if div == 0:
                            continue #Parallel, might be on edge

                        #t = (q-p)xs/div
                        t = ((ox1-x1)*oy2 - (oy1-y1)*ox2)/div
                        #u = (q-p)xr/div
                        u = ((ox1-x1)*y2 - (oy1-y1)*x2)/div

                        if 0 <= t <= 1 and 0 <= u <= 1:
                            print 'Collision detected'
                            return True
        return False

    #TODO: Make sensor continuous, and work for polygon obstacles
    def sensor(self, car):
        x = car.sensors[0].x
        y = car.sensors[0].y
        angle = car.sensors[0].angle
        length = car.sensors[0].length

        closest = length

        x1 = x
        y1 = y
        x2 = np.sin(angle) * length
        y2 = - np.cos(angle) * length

        for obs in self.obstacles:
            obs_coords = obs.points[:]
            obs_coords.append(obs_coords[0])
            for j in range(len(obs_coords) - 1):
                ox1 = obs_coords[j][0]
                oy1 = obs_coords[j][1]
                ox2 = obs_coords[j + 1][0] - ox1
                oy2 = obs_coords[j + 1][1] - oy1

                #rxs
                div = x2 * oy2 - y2 * ox2

                if div == 0:
                    continue #Parallel, might be on edge

                #t = (q-p)xs/div
                t = ((ox1-x1)*oy2 - (oy1-y1)*ox2)/div
                #u = (q-p)xr/div
                u = ((ox1-x1)*y2 - (oy1-y1)*x2)/div

                if 0 <= t <= 1 and 0 <= u <= 1:
                    closest = min(closest, length*t)
        print 'Sensor firing: ' + str(closest)
        car.sensor_inputs = [closest]
        car.sensors[0].fire = closest
        return closest

    def iterate(self):
        for car in self.cars:
            car.iterate_dynamics()
            
            #temprary
            self.sensor(car)

        self.detect_collision()


class Obstacle:

    #Every obstacle is defined as a polygon of points, end -> start implied
    def __init__(self, points):
        self.points = points

