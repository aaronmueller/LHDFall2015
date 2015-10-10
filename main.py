# Menu

# draw the menu

from graphics import *


def main():

    # size = input("What size screen do you want? (Small, Medium, Large, Full): ")
    width = 800
    height = 600

    winMenu = GraphWin("", 800, 600)

    title = Text(Point((winMenu.getWidth() / 2), 10), "Welcome to the Multiplayer Snake Game")
    title.setSize(15)
    title.draw(winMenu)

    options = Text(Point((winMenu.getWidth() / 2), 110), "Options")
    options.setSize(15)
    options.draw(winMenu)

    play = Text(Point((winMenu.getWidth() / 2), 210), "PLAY")
    play.setSize(20)
    play.draw(winMenu)

    
    point1 = winMenu.getMouse()
    point1x = point1.getX()
    point1y = point1.getY()

    if((point1y > 100)and(point1y < 120)):
        title.undraw()
        play.undraw()
        options.undraw()

        optionsMenu = Text(Point((winMenu.getWidth() / 2), 10), "Options")
        optionsMenu.setSize(15)
        screenSmall = Text(Point((winMenu.getWidth() / 2), 100), "Small")
        screenMedium = Text(Point((winMenu.getWidth() / 2), 200), "Medium")
        screenLarge = Text(Point((winMenu.getWidth() / 2), 300), "Large")
        back = Text(Point((winMenu.getWidth() / 2), 450), "BACK")
        optionsMenu.draw(winMenu)
        screenSmall.draw(winMenu)
        screenMedium.draw(winMenu)
        screenLarge.draw(winMenu)
        back.draw(winMenu)
        
        

        point2 = winMenu.getMouse()
        point2x = point2.getX()
        point2y = point2.getY()
        

        while((point2y <= 90)and(point2y >= 100)):

            if((point2y > 90)and(point2y < 100)):
                width = 800
                height = 600

            elif((point2y > 190)and(point2y < 210)):
                width = 1024
                height = 768

            elif((point2y > 290)and(point2y < 310)):
                width = 1920
                height = 1080

            point2 = winMenu.getMouse()
            point2x = point2.getX()
            point2y = point2.getY()

        if((point2y > 440)and(point2y < 460)):
            optionsMenu.undraw()
            screenSmall.undraw()
            screenMedium.undraw()
            screenLarge.undraw()

            title.draw(winMenu)
            options.draw(winMenu)
            play.draw(winMenu)

    elif((point1y > 200)and(point1y < 220)):
        title.undraw()
        options.undraw()
        
        winGame = GraphWin("Game", width, height)

        yes = Text(Point(100,100), "YAY")
        yes.draw(winGame)

    winMenu.getMouse()
    winMenu.close()

main()

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
