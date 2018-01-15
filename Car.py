import numpy as np

'''
ANN inputs
sensor1
sensor2
sensor3
current velocity
current wheel position
current power

ANN outputs
absolute power
absolute wheel position

1 hidden layer, 8-ish neurons
'''

class Car:

    def __init__(self):
        #Car size and rotation
        #Position is absolute center of car
        self.x = 300
        self.y = 300
        self.l = 30
        self.w = 16
        self.angle = np.pi/16.0

        #Car dynamics
        self.velocity = 0
        self.acceleration = 0
        self.wheel = np.pi/64.0

        self.max_turn = np.pi/50.0
        self.max_acceleration = 2
        self.max_velocity = 5

        #Sensor configuration
        self.sensor_length = 200
        self.sensors = [
                Sensor(self, self.sensor_length, 0),
                Sensor(self, self.sensor_length, -np.pi/4.0),
                Sensor(self, self.sensor_length, np.pi/4.0),
                ]
        self.sensor_inputs = [self.sensor_length for _ in self.sensors]

        #Neural network
        self.layer1 = [0.01, -0.5]
        self.thresh1 = -0.3
        self.layer2 = []
        self.thresh2 = 0

        self.ANNout = []

    #Returns a list of 4 tuples containing (x, y) of car corners
    def get_car_boundaries(self):
        corner_angle = np.arctan(float(self.w)/float(self.l))

        diag = np.sqrt(self.w**2/4.0 + self.l**2/4.0)

        x1 = self.x + np.sin(self.angle + corner_angle)*diag
        x2 = self.x + np.sin(self.angle + np.pi - corner_angle)*diag
        x3 = self.x + np.sin(self.angle + np.pi + corner_angle)*diag
        x4 = self.x + np.sin(self.angle - corner_angle)*diag

        y1 = self.y + np.cos(self.angle + corner_angle)*diag
        y2 = self.y + np.cos(self.angle + np.pi - corner_angle)*diag
        y3 = self.y + np.cos(self.angle + np.pi + corner_angle)*diag
        y4 = self.y + np.cos(self.angle - corner_angle)*diag

        return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

    #Implemented a pretty simple model which uses the wheel position to continuously update the angle of the car
    #The positions are then updated according to 
    def iterate_dynamics(self):
        acc = min(self.max_acceleration, max(-self.max_acceleration, self.acceleration))
        if not abs(self.velocity) > self.max_velocity:
            self.velocity += acc

        self.angle += min(self.max_turn, max(-self.max_turn, self.wheel))

        self.x += self.velocity*np.sin(self.angle)
        self.y += self.velocity*np.cos(self.angle)

        #Sensor updates, actual sensor tracking is done from track
        for i, sensor in enumerate(self.sensors):
            sensor.update_sensor_position()
            self.sensor_inputs[i] = self.sensors[i].fire

        self.propagate_network()

    #TODO: Inputs from sensors should follow an exponential pattern rather than a linear
    def propagate_network(self):
        self.acceleration = (self.layer1[0] * self.sensor_inputs[0] + self.layer1[1] * self.velocity) + self.thresh1

class Sensor:

    def __init__(self, car, length, rel_angle):
        self.car = car
        self.length = length
        self.rel_angle = rel_angle

        self.update_sensor_position()
        self.fire = length

    def update_sensor_position(self):
        self.x = self.car.x
        self.y = self.car.y
        self.angle = self.car.angle + self.rel_angle

