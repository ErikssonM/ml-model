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
        self.x = 400
        self.y = 200
        self.angle = np.pi

        self.l = 30
        self.w = 16

        self.velocity = 0
        self.acceleration = 0
        self.wheel = 0

        self.sensor_length = 100
        self.sensor_inputs = [self.sensor_length]

        self.layer1 = [0.01, -0.2]
        self.thresh1 = -0.5
        self.layer2 = []
        self.thresh2 = 0

    #TODO: Work out and implement proper dynamics for car
    def iterate_dynamics(self):
        acc = min(2, max(-2, self.acceleration))
        if not abs(self.velocity) > 10:
            self.velocity += acc
        self.y += self.velocity

        self.propagate_network()

    def propagate_network(self):
        self.acceleration = (self.layer1[0] * self.sensor_inputs[0] + self.layer1[1] * self.velocity) + self.thresh1
        #self.acceleration = self.layer1[0] * self.sensor_inputs[0]
        print self.velocity

    def update_weights(self):
        pass
