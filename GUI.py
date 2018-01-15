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
            self.c.create_polygon(obs.points)

    #TODO: Make it possible to render sensors and the points where they fire
    def render_cars(self, cars):
        for i in self.car_polygons:
            self.c.delete(i)
        self.car_polygons = []
        for car in cars: 
            coords = car.get_car_boundaries()
            i = self.c.create_polygon(coords, fill='blue')
            self.car_polygons.append(i)
