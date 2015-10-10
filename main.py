# Menu

# draw the menu

from graphics import *

def main():

    # size = input("What size screen do you want? (Small, Medium, Large, Full): ")
    width = 800
    height = 600

    winMenu = GraphWin("Snakes", 800, 600)

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

        optionsMenu = Text(Point((winMenu.getWidth() / 2), 10), "Options")
        screenSmall = Text(Point((winMenu.getWidth() / 2), 100), "Small")
        screenMedium = Text(Point((winMenu.getWidth() / 2), 200), "Medium")
        screenLarge = Text(Point((winMenu.getWidth() / 2), 300), "Large")
        back = Text(Point((winMenu.getWidth() / 2), 450), "BACK")

        point2 = winMenu.getMouse()
        point2x = point2.getX()
        point2y = point2.getY()

        if((point1y > 90)and(point1y < 100)):
            width = 800
            height = 600

        elif((point1y > 190)and(point1y < 210)):
            width = 1024
            height = 768

        elif((point1y > 290)and(point1y < 310)):
            width = 1920
            height = 1080

        elif((point1y > 440)and(point1y < 460)):
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
