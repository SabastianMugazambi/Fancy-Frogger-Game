# interfaces.py
# A module containing two interfaces for the lunar lander game.
#
# Please mess around with this program, have fun with this game!
#
# by Andy Exley
#

from graphics import *

class TextLanderInterface:
    """Text-based interface for lander game. Use this one for testing"""

    def show_info(self, lander):
        print ("Lander Status: Altitude %d, Velocity %d, Fuel %d" % 
            (lander.get_altitude(), lander.get_velocity(), lander.get_fuel()))

    def get_thrust(self):
        amtstr = raw_input("Thrust amount? ")
        return int(amtstr)

    def show_crash(self):
        print "Crash! Oh noes!"

    def show_landing(self):
        print "Hooray, the Eagle has landed!"

    def close(self):
        print "Goodbye"

class GraphicLanderInterface:
    """GraphicLanderInterface class is a graphical interface 
        for your lunar lander game"""

    def __init__(self):
        """Constructor that initializes the graphics window
        and shapes that we will use for drawing things"""

        # initialize window
        self.window = GraphWin("Lunar Lander Game", 300, 500)
        # transform coordinates
        self.window.setCoords(0, -10, 300, 600)

        self.surface_polygon = self.create_surface()
        self.surface_polygon.draw(self.window)

        self.lander_polygon = None

    def show_info(self, lander):
        """This method currently gets the lander info then draws it.
        That's it. It doesn't actually show any information."""
        alt = lander.get_altitude()

        # if lander polygon is drawn, undraw it
        if self.lander_polygon:
            self.lander_polygon.undraw()
        self.lander_polygon = Polygon(Point(self.window.width / 2 - 10, alt),
                Point(self.window.width/2 - 3, alt + 10),
                Point(self.window.width/2 + 3, alt + 10),
                Point(self.window.width/2 + 10, alt))
        self.lander_polygon.setFill("blue")
        self.lander_polygon.draw(self.window)

    def get_thrust(self):
        """This method waits for a user's mouse click then returns 0 thrust
            amount. You'll want to fix this to avoid catastrophic incidents."""
        self.window.getMouse()
        return 0

    def show_crash(self):
        """Crash message... change this to graphical message"""
        print "Crash! Oh noes!"

    def show_landing(self):
        """Landing message... change this to graphical message"""
        print "Hooray, the Eagle has landed!"

    def close(self):
        self.window.close()

    def create_surface(self):
        """Draws the surface of the moon"""
        rect = Rectangle(Point(5,0),Point(300,-10))
        rect.setFill("gray")
        return rect
