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

    def render_cars(self, cars):
        for i in self.car_polygons:
            self.c.delete(i)
        self.car_polygons = []
        for car in cars: 
            coords = car.get_car_boundaries()
            i = self.c.create_polygon(coords, fill='blue')
            self.car_polygons.append(i)

            for sensor in car.sensors:
                x1 = sensor.x
                y1 = sensor.y
                x2 = sensor.x + sensor.length*np.sin(sensor.angle)
                y2 = sensor.y + sensor.length*np.cos(sensor.angle)
                fire_x = sensor.x + sensor.fire*np.sin(sensor.angle)
                fire_y = sensor.y + sensor.fire*np.cos(sensor.angle)

                i = self.c.create_line(x1, y1, x2, y2)
                self.car_polygons.append(i)

                i = self.c.create_oval(fire_x-5, fire_y-5, fire_x+5, fire_y+5, fill='red')
                self.car_polygons.append(i)
