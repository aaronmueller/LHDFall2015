# Local Hack Day
# Aaron Mueller and Jacob Pawlak
# October 10

from graphics import *

def game():

    win = GraphWin("Game", 500, 500)
    win.setBackground("#EFDECD")

    bike1 = Rectangle(Point(1,1),Point(15,15))
    bike1.setFill("#CCCCFF")
    bike1.draw(win)

    for i in range(3):
   
        win.getMouse()
        bike1.move(15,0)

        win.getMouse()

        bike1.move(0,15)

    win.getMouse()

    bike1.undraw()

    win.close()

game()
