from Car import Car
from Track import Track
from GUI import GUI

#General TODO:
#

if __name__ == '__main__':
    cars = [Car(), Car(), Car(), Car(), Car(), Car(), Car(), Car(), Car(), Car()]
    track = Track()
    track.add_cars(cars)
    g = GUI(track)

    def render_loop():

        if track.iterate():
            g.render(track)
            g.master.after(50, render_loop)
        else:
            g.quit()

    render_loop()

    g.master.mainloop()


    
