from Car import Car
from Track import Track
from GUI import GUI

#General TODO:
#

if __name__ == '__main__':
    cars = [Car()]
    track = Track(cars)
    g = GUI(track)

    def render_loop():

        track.iterate()

        g.render(track)
        g.master.after(50, render_loop)

    render_loop()

    g.master.mainloop()

    
