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
        self.obstacles.append(Obstacle(400, 400, 200, 20))

    #TODO: Car hitbox is wrong
    #TODO: Make it work with polygon obstacles
    def detect_collision(self):
        for car in self.cars:
            cx1 = car.x - car.l/2
            cx2 = car.x + car.l/2

            cy1 = car.y - car.l/2
            cy2 = car.y + car.l/2

            for obs in self.obstacles:
                ox1 = obs.x - obs.w/2
                ox2 = obs.x + obs.w/2

                oy1 = obs.y - obs.h/2
                oy2 = obs.y + obs.h/2

                if ((ox1 < cx1 and cx1 < ox2 and oy1 < cy1 and cy1 < oy2)
                    or (ox1 < cx2 and cx2 < ox2 and oy1 < cy1 and cy1 < oy2) 
                    or (ox1 < cx2 and cx2 < ox2 and oy1 < cy2 and cy2 < oy2) 
                    or (ox1 < cx1 and cx1 < ox2 and oy1 < cy2 and cy2 < oy2)):
                    print 'Collision detected'



    #TODO: Make sensor continuous, and work for polygon obstacles
    def sensor(self, car):
        x = car.x
        y = car.y
        angle = car.angle
        length = car.sensor_length

        car.sensor_inputs[0] = length

        step_length = length/10.0
        steps = [step_length * i for i in range(1, 11)]
        for s in steps:
            sx = x + s * np.sin(angle) #TODO: might be wrong
            sy = y - s * np.cos(angle)
            for obs in self.obstacles:
                ox1 = obs.x - obs.w/2
                ox2 = obs.x + obs.w/2

                oy1 = obs.y - obs.h/2
                oy2 = obs.y + obs.h/2

                if (ox1 < sx < ox2 and oy1 < sy < oy2):
                    car.sensor_inputs[0] = s


    def iterate(self):
        for car in self.cars:
            car.iterate_dynamics()
            
            #temprary
            self.sensor(car)

        self.detect_collision()


class Obstacle:

    #TODO: Redefine to be generalized polygon
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        #self.rot = rot
