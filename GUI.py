from Tkinter import *
from Track import Track, Obstacle
from Car import Car
from random import randint
import numpy as np

class GUI:

    def __init__(self, track):
        self.master = Tk()
        self.c = Canvas(self.master, width=800, height=800)
        self.c.pack()

        self.render_obstacles(track.obstacles)

        self.car_polygons = []

        self.track = track

    def render(self, track):
        self.render_cars(track.cars)

    def render_obstacles(self, obstacles):
        for obs in obstacles:
            x1 = obs.x - obs.w/2
            x2 = obs.x + obs.w/2
            y1 = obs.y - obs.h/2
            y2 = obs.y + obs.h/2
            self.c.create_polygon(x1, y1, x2, y1, x2, y2, x1, y2)

    def render_cars(self, cars):
        for i in self.car_polygons:
            self.c.delete(i)
        self.car_polygons = []
        for car in cars: 
            x1 = car.x - car.w/2
            x2 = car.x + car.w/2
            y1 = car.y - car.l/2
            y2 = car.y + car.l/2
            i = self.c.create_polygon(x1, y1, x2, y1, x2, y2, x1, y2, fill='blue')
            self.car_polygons.append(i)
