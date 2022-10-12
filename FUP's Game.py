#########################
# Ruan Henrique Cardoso #
#   Matrícula: 535786   #
#########################

import time
import turtle
import pygame
from pygame import mixer
from math import sqrt
from random import randint

def Writer(where, what, color, title):
    xy = [(-175, 200), (0, 200), (175, 200),
          (-175, 0), (0, 0), (175, 0),
          (-175, -200), (0, -200), (175, -200)]

    turtle.penup()
    turtle.goto(xy[where])
    turtle.hideturtle()
    if title is False:
        turtle.color(color)
        turtle.write(what, True, align='center', font=("Anticode", 14, "normal"))
    else:
        turtle.color(color)
        turtle.write(what, True, align='center', font=("Anticode", 20, "normal"))

def Menu():
    screen.title("FUP's Game")
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0, 0)

    mixer.stop()
    mixer.music.load("Songs/Menu/BackgroundMenu.mp3")
    mixer.music.play(-1)
    background = turtle.Turtle()
    background.shape("Images/Menu/menuImage.gif")

    Writer(4, "Space Symphony", "white", True)
    Writer(7, "Start\n Exit", "white", False)


    turtle.goto(0, 270)
    turtle.write("You're beginning an Adventure, rest, feel this energy.",
                 True, align='center', font=("Glitch Inside", 11, "normal"))
    turtle.goto(0, -300)
    turtle.write("Press 0/1 to turn off/on music", True, align='center', font=("Anticode", 11, "normal"))
    screen.update()

    def Mute():
        mixer.music.set_volume(0)
    def Unmute():
        mixer.music.set_volume(100)

    turtle.onkey(Exit, "Escape")
    turtle.onkey(Tutorial, "Return")
    turtle.onkey(Tutorial, "space")
    turtle.onkey(Mute, "0")
    turtle.onkey(Unmute, "1")

    turtle.listen()
def Tutorial():
    screen.title("Tutorial.")
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0, 0)

    background = turtle.Turtle()
    background.shape("Images/Backgrounds/starfieldBackground1.gif")
    selectedOption = mixer.Sound("Songs/Menu/SelectedOption.wav")
    selectedOption.play()

    energyShapes = ["Images/OnGame/Obstacles/Energy/Energy1.gif", "Images/OnGame/Obstacles/Energy/Energy2.gif",
                    "Images/OnGame/Obstacles/Energy/Energy3.gif", "Images/OnGame/Obstacles/Energy/Energy4.gif"]
    asteroidShapes = ["Images/OnGame/Obstacles/Asteroids/Rock1.gif", "Images/OnGame/Obstacles/Asteroids/Rock2.gif",
                      "Images/OnGame/Obstacles/Asteroids/Rock3.gif", "Images/OnGame/Obstacles/Asteroids/Rock4.gif",
                      "Images/OnGame/Obstacles/Asteroids/Rock5.gif", "Images/OnGame/Obstacles/Asteroids/Rock6.gif",
                      "Images/OnGame/Obstacles/Asteroids/Rock7.gif", "Images/OnGame/Obstacles/Asteroids/Rock8.gif"]
    spaceshipsShapes = ["Images/OnGame/Spaceships/spaceShip4.gif", "Images/OnGame/Spaceships/spaceShip5.gif",
                        "Images/OnGame/Spaceships/spaceShip6.gif"]

    def tutorialText():
        turtle.penup()
        turtle.color("white")
        turtle.goto(0, 200)
        turtle.write("TUTORIAL", True, align='center', font=("Anticode", 20, "normal"))

        turtle.goto(-175, 85)
        turtle.write("Asteroids", True, align='center', font=("Anticode", 16, "normal"))
        turtle.goto(-175, -165,)
        turtle.write("  Lose 20 energy\n if it touches you.", True, align='center', font=("Anticode", 14, "normal"))

        turtle.goto(175, 85)
        turtle.write("Energy", True, align='center', font=("Anticode", 16, "normal"))
        turtle.goto(175, -165)
        turtle.write("  Get 20 energy\n if you touches it.", True, align='center', font=("Anticode", 14, "normal"))

        turtle.goto(0, 100)
        turtle.write("You", True, align='center', font=("Anticode", 16, "normal"))

        turtle.goto(0, -300)
        turtle.write("Press SPACE to continue or ESC o exit", True, align='center', font=("Anticode", 14, "normal"))
    def loadObstacles():
        obstacle0 = turtle.Turtle()
        obstacle0.penup()
        obstacle0.goto(-240, -15)
        obstacle0.shape(asteroidShapes[0])

        obstacle1 = turtle.Turtle()
        obstacle1.penup()
        obstacle1.goto(-170, 35)
        obstacle1.shape(asteroidShapes[3])

        obstacle2 = turtle.Turtle()
        obstacle2.penup()
        obstacle2.goto(-100, -15)
        obstacle2.shape(asteroidShapes[5])

        obstacle3 = turtle.Turtle()
        obstacle3.penup()
        obstacle3.goto(-170, -65)
        obstacle3.shape(asteroidShapes[7])
    def loadEnergies():
        energy0 = turtle.Turtle()
        energy0.penup()
        energy0.goto(240, -15)
        energy0.shape(energyShapes[0])
        energy1 = turtle.Turtle()
        energy1.penup()
        energy1.goto(170, 35)
        energy1.shape(energyShapes[1])
        energy2 = turtle.Turtle()
        energy2.penup()
        energy2.goto(100, -15)
        energy2.shape(energyShapes[2])
        energy3 = turtle.Turtle()
        energy3.penup()
        energy3.goto(170, -65)
        energy3.shape(energyShapes[3])
    def loadSpaceships():
        spaceship0 = turtle.Turtle()
        spaceship0.penup()
        spaceship0.goto(0, 50)
        spaceship0.shape(spaceshipsShapes[0])
        spaceship0.showturtle()

        spaceship1 = turtle.Turtle()
        spaceship1.penup()
        spaceship1.goto(0, -50)
        spaceship1.shape(spaceshipsShapes[1])
        spaceship1.showturtle()

        spaceship2 = turtle.Turtle()
        spaceship2.penup()
        spaceship2.goto(0, -150)
        spaceship2.shape(spaceshipsShapes[2])
        spaceship2.showturtle()

    tutorialText()
    loadObstacles()
    loadEnergies()
    loadSpaceships()

    turtle.showturtle()

    turtle.listen()
    turtle.onkey(Menu, "Escape")
    turtle.onkey(chooseSpaceship, "Return")
    turtle.onkey(chooseSpaceship, "space")

    screen.update()
def Exit():
    screen.title("Exit!")
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0, 0)

    background = turtle.Turtle()
    background.shape("Images/Backgrounds/starfieldBackground2.gif")
    selectedOption = mixer.Sound("Songs/Menu/SelectedOption2.wav")
    selectedOption.play()

    Writer(4, "R u sure that u wanna exit?", "white", True)
    Writer(7, "\n Y/N", "white", True)
    screen.update()

    def closeProgram():
        exit()

    turtle.listen()
    turtle.onkey(Menu, "n")
    turtle.onkey(Menu, "N")
    turtle.onkey(closeProgram, "y")
    turtle.onkey(closeProgram, "Y")

def Images():
    screen.addshape("Images/Menu/menuImage.gif")
    screen.addshape("Images/Menu/Egg.gif")
    screen.addshape("Images/Spaceships/spaceShip4.gif")
    screen.addshape("Images/Spaceships/spaceShip5.gif")
    screen.addshape("Images/Spaceships/spaceShip6.gif")
    screen.addshape("Images/Backgrounds/playingBackground.gif")
    screen.addshape("Images/Backgrounds/sideWallRight.gif")
    screen.addshape("Images/Backgrounds/sideWallLeft.gif")
    screen.addshape("Images/Backgrounds/starfieldBackground1.gif")
    screen.addshape("Images/Backgrounds/starfieldBackground2.gif")
    screen.addshape("Images/Backgrounds/starfieldBackground3.gif")
    screen.addshape("Images/Backgrounds/starfieldBackground4.gif")
    screen.addshape("Images/OnGame/Spaceships/spaceShip1.gif")
    screen.addshape("Images/OnGame/Spaceships/spaceShip2.gif")
    screen.addshape("Images/OnGame/Spaceships/spaceShip3.gif")
    screen.addshape("Images/OnGame/Spaceships/spaceShip4.gif")
    screen.addshape("Images/OnGame/Spaceships/spaceShip5.gif")
    screen.addshape("Images/OnGame/Spaceships/spaceShip6.gif")
    screen.addshape("Images/OnGame/Obstacles/Energy/Energy1.gif")
    screen.addshape("Images/OnGame/Obstacles/Energy/Energy2.gif")
    screen.addshape("Images/OnGame/Obstacles/Energy/Energy3.gif")
    screen.addshape("Images/OnGame/Obstacles/Energy/Energy4.gif")
    screen.addshape("Images/OnGame/Obstacles/Asteroids/Rock1.gif")
    screen.addshape("Images/OnGame/Obstacles/Asteroids/Rock2.gif")
    screen.addshape("Images/OnGame/Obstacles/Asteroids/Rock3.gif")
    screen.addshape("Images/OnGame/Obstacles/Asteroids/Rock4.gif")
    screen.addshape("Images/OnGame/Obstacles/Asteroids/Rock5.gif")
    screen.addshape("Images/OnGame/Obstacles/Asteroids/Rock6.gif")
    screen.addshape("Images/OnGame/Obstacles/Asteroids/Rock7.gif")
    screen.addshape("Images/OnGame/Obstacles/Asteroids/Rock8.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar0.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar1.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar2.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar3.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar4.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar5.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar6.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar7.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar8.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar9.gif")
    screen.addshape("Images/OnGame/EnergyBar/EnergyBar10.gif")

def chooseSpaceship():
    screen.title("Choose your spaceship!")
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0, 0)

    background = turtle.Turtle()
    background.shape("Images/Backgrounds/starfieldBackground1.gif")
    selectedOption = mixer.Sound("Songs/Menu/SelectedOption.wav")
    selectedOption.play()

    ship1 = turtle.Turtle()
    ship1.hideturtle()
    ship1.penup()
    ship1.goto(-180, 0)
    ship1.shape("Images/Spaceships/spaceShip4.gif")
    ship1.showturtle()

    ship2 = turtle.Turtle()
    ship2.hideturtle()
    ship2.penup()
    ship2.goto(0, 0)
    ship2.shape("Images/Spaceships/spaceShip5.gif")
    ship2.showturtle()

    ship3 = turtle.Turtle()
    ship3.hideturtle()
    ship3.penup()
    ship3.goto(180, 0)
    ship3.shape("Images/Spaceships/spaceShip6.gif")
    ship3.showturtle()

    Writer(1, "Choose your spaceship!", "white", True)
    Writer(6, "    Press 1\n To choose", "white", False)
    Writer(7, "    Press 2\n To choose", "white", False)
    Writer(8, "    Press 3\n To choose", "white", False)
    turtle.goto(0, -325)
    turtle.write("Press ESC to back", True, align='center', font=("Anticode", 12, "normal"))
    screen.update()

    def setSpaceship4():
        selectedSpaceship("Images/Spaceships/spaceShip4.gif")
    def setSpaceship5():
        selectedSpaceship("Images/Spaceships/spaceShip5.gif")
    def setSpaceship6():
        selectedSpaceship("Images/Spaceships/spaceShip6.gif")

    turtle.listen()
    turtle.onkey(Tutorial, "Escape")
    turtle.onkey(setSpaceship4, "1")
    turtle.onkey(setSpaceship5, "2")
    turtle.onkey(setSpaceship6, "3")
def selectedSpaceship(shape):
    screen.title("Spaceship Selected")
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0, 0)

    background = turtle.Turtle()
    background.shape("Images/Backgrounds/starfieldBackground1.gif")
    selectedOption = mixer.Sound("Songs/Menu/SelectedOption.wav")
    selectedOption.play()

    ship = turtle.Turtle()
    ship.hideturtle()
    ship.penup()
    ship.goto(0, 0)
    ship.showturtle()
    ship.shape(shape)

    shipNumber = 0
    match shape:
        case "Images/Spaceships/spaceShip6.gif":
            shipNumber = 3
            shape = "Images/OnGame/Spaceships/spaceShip6.gif"
        case "Images/Spaceships/spaceShip5.gif":
            shipNumber = 2
            shape = "Images/OnGame/Spaceships/spaceShip5.gif"
        case "Images/Spaceships/spaceShip4.gif":
            shipNumber = 1
            shape = "Images/OnGame/Spaceships/spaceShip4.gif"

    Writer(1, f"You selected spaceship {shipNumber}!", "white", True)
    Writer(7, "Press SPACE to start", "white", True)


    turtle.goto(0, -325)
    turtle.color('white')
    turtle.write("Press ESC to back", True, align='center', font=("Anticode", 12, "normal"))

    def callGame():
        Game(shape)

    turtle.listen()
    turtle.onkey(chooseSpaceship, "Escape")
    turtle.onkey(callGame, "space")

    screen.update()

def Game(selectedShape):
    screen.title("Playing.")
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0, 0)
    mixer.music.stop()

    global startTime
    global score
    global energy
    global player
    global energyBar
    global asteroid0
    global asteroi1
    global energyRefil
    global difficulty

    xCor = [randint(-250, 0), randint(0, 250), randint(-250, 250), randint(-250, 250)]
    yCor = [randint(-350, 0), randint(0, 350)]
    energy = 100
    difficulty = 0
    startTime = time.time()
    score = 000
    energyShapes = ["Images/OnGame/Obstacles/Energy/Energy1.gif", "Images/OnGame/Obstacles/Energy/Energy2.gif",
                    "Images/OnGame/Obstacles/Energy/Energy3.gif", "Images/OnGame/Obstacles/Energy/Energy4.gif"]
    asteroidShapes = ["Images/OnGame/Obstacles/Asteroids/Rock1.gif", "Images/OnGame/Obstacles/Asteroids/Rock2.gif",
                      "Images/OnGame/Obstacles/Asteroids/Rock3.gif", "Images/OnGame/Obstacles/Asteroids/Rock4.gif",
                      "Images/OnGame/Obstacles/Asteroids/Rock5.gif", "Images/OnGame/Obstacles/Asteroids/Rock6.gif",
                      "Images/OnGame/Obstacles/Asteroids/Rock7.gif", "Images/OnGame/Obstacles/Asteroids/Rock8.gif"]
    energyBarShape = ["Images/OnGame/EnergyBar/EnergyBar0.gif", "Images/OnGame/EnergyBar/EnergyBar1.gif",
                      "Images/OnGame/EnergyBar/EnergyBar2.gif", "Images/OnGame/EnergyBar/EnergyBar3.gif",
                      "Images/OnGame/EnergyBar/EnergyBar4.gif", "Images/OnGame/EnergyBar/EnergyBar5.gif",
                      "Images/OnGame/EnergyBar/EnergyBar6.gif", "Images/OnGame/EnergyBar/EnergyBar7.gif",
                      "Images/OnGame/EnergyBar/EnergyBar8.gif", "Images/OnGame/EnergyBar/EnergyBar9.gif",
                      "Images/OnGame/EnergyBar/EnergyBar10.gif"]

    def Background():
        global background1
        global background2
        global leftWall1
        global leftWall2
        global rightWall1
        global rightWall2

        background1 = turtle.Turtle()
        background2 = turtle.Turtle()
        background1.shape("Images/Backgrounds/playingBackground.gif")
        background2.shape("Images/Backgrounds/playingBackground.gif")
        background2.sety(800)

        leftWall1 = turtle.Turtle()
        leftWall1.hideturtle()
        leftWall1.penup()
        leftWall1.goto(275, 10)
        leftWall1.shape("Images/Backgrounds/sideWallLeft.gif")
        leftWall1.showturtle()
        leftWall2 = turtle.Turtle()
        leftWall2.hideturtle()
        leftWall2.penup()
        leftWall2.goto(275, 10)
        leftWall2.shape("Images/Backgrounds/sideWallLeft.gif")
        leftWall2.showturtle()

        rightWall1 = turtle.Turtle()
        rightWall1.hideturtle()
        rightWall1.penup()
        rightWall1.goto(-275, 10)
        rightWall1.shape("Images/Backgrounds/sideWallRight.gif")
        rightWall1.showturtle()
        rightWall2 = turtle.Turtle()
        rightWall2.hideturtle()
        rightWall2.penup()
        rightWall2.goto(-275, 10)
        rightWall2.shape("Images/Backgrounds/sideWallRight.gif")
        rightWall2.showturtle()
    def runningBackground():
        global background1
        global background2
        global leftWall1
        global leftWall2
        global rightWall1
        global rightWall2

        screen.tracer(0, 0)
        background1.penup()
        background2.penup()
        leftWall1.penup()
        leftWall2.penup()
        rightWall1.penup()
        rightWall2.penup()

        if background1.ycor() >= -800:
            background1.sety(background1.ycor() - 2)
        elif background1.ycor() < -800:
            background1.sety(0)
        if background2.ycor() >= 0:
            background2.sety(background2.ycor() - 2)
        elif background2.ycor() < 0:
            background2.sety(800)

        if leftWall1.ycor() >= -800:
            leftWall1.sety(leftWall1.ycor() - 3)
        elif leftWall1.ycor() < -800:
            leftWall1.sety(0)
        if leftWall2.ycor() >= 0:
            leftWall2.sety(leftWall2.ycor() - 3)
        elif leftWall2.ycor() < 0:
            leftWall2.sety(800)

        if rightWall1.ycor() >= -800:
            rightWall1.sety(rightWall1.ycor() - 3)
        elif rightWall1.ycor() < -800:
            rightWall1.sety(0)
        if rightWall2.ycor() >= 0:
            rightWall2.sety(rightWall2.ycor() - 3)
        elif rightWall2.ycor() < 0:
            rightWall2.sety(800)

        screen.update()
    def setObjectsOnBackground():
        global asteroid0
        asteroid0 = turtle.Turtle()
        asteroid0.hideturtle()
        asteroid0.penup()
        asteroid0.goto(xCor[0], 550)
        asteroid0.showturtle()
        asteroid0.shape(asteroidShapes[randint(0, 7)])

        global asteroid1
        asteroid1 = turtle.Turtle()
        asteroid1.hideturtle()
        asteroid1.penup()
        asteroid1.goto(xCor[1], 750)
        asteroid1.showturtle()
        asteroid1.shape(asteroidShapes[randint(0, 7)])

        global asteroid2
        asteroid2 = turtle.Turtle()
        asteroid2.hideturtle()
        asteroid2.penup()
        asteroid2.goto(xCor[2], 550)
        asteroid2.showturtle()
        asteroid2.shape(asteroidShapes[randint(0, 7)])

        global asteroid3
        asteroid3 = turtle.Turtle()
        asteroid3.hideturtle()
        asteroid3.penup()
        asteroid3.goto(xCor[2], 750)
        asteroid3.showturtle()
        asteroid3.shape(asteroidShapes[randint(0, 7)])

        global asteroid4
        asteroid4 = turtle.Turtle()
        asteroid4.hideturtle()
        asteroid4.penup()
        asteroid4.goto(350, yCor[1])
        asteroid4.showturtle()
        asteroid4.shape(asteroidShapes[randint(0, 7)])

        global energyRefil
        energyRefil = turtle.Turtle()
        energyRefil.hideturtle()
        energyRefil.penup()
        energyRefil.goto(xCor[3], 400)
        energyRefil.showturtle()
        energyRefil.shape(energyShapes[randint(0, 3)])

        global energyBar
        energyBar = turtle.Turtle()
        energyBar.hideturtle()
        energyBar.penup()
        energyBar.goto(175, 250)
        energyBar.showturtle()
        energyBar.shape(energyBarShape[10])

    def Panel(Up, Down):
        global startTime
        global score
        global difficulty

        endTime = time.time()
        elapsedTime = int(endTime - startTime)

        if Up == 20:
            score += Up + (2 * difficulty)
        elif Down == 20:
            score -= Down + (5 * difficulty)
        else:
            score += elapsedTime + difficulty

        if score < 0:
            score = 0

        if score >= 500:
            difficulty = 1
        if score >= 2000:
            difficulty = 2
        if score >= 7000:
            difficulty = 3
        if score >= 15000:
            difficulty = 4
        if score >= 25000:
            difficulty = 5
    def Player():
        global player
        player = turtle.Turtle()
        player.hideturtle()
        player.penup()
        player.goto(0, -200)
        player.left(90)
        player.shape(selectedShape)
        player.showturtle()

        def Right():
            player.setx((player.xcor() + (15 + difficulty)))
        def Left():
            player.setx((player.xcor() - (15 + difficulty)))
        def Up():
            player.sety((player.ycor() + (15 + difficulty)))
        def Down():
            player.sety((player.ycor() - (15 + difficulty)))

        acceptableKeys = ["d", "D", "Right", "a", "A", "Left", "w", "W", "Up", "s", "S", "Down"]
        turtle.listen()

        turtle.onkeypress(Right, acceptableKeys[0])
        turtle.onkeypress(Right, acceptableKeys[1])
        turtle.onkeypress(Right, acceptableKeys[2])
        turtle.onkeypress(Left, acceptableKeys[3])
        turtle.onkeypress(Left, acceptableKeys[4])
        turtle.onkeypress(Left, acceptableKeys[5])
        turtle.onkeypress(Up, acceptableKeys[6])
        turtle.onkeypress(Up, acceptableKeys[7])
        turtle.onkeypress(Up, acceptableKeys[8])
        turtle.onkeypress(Down, acceptableKeys[9])
        turtle.onkeypress(Down, acceptableKeys[10])
        turtle.onkeypress(Down, acceptableKeys[11])

    def spaceshipEnergy(Up, Down):
        global energy
        global startTime

        elapsedTime = 0
        energy -= elapsedTime
        energy -= Down
        energy += Up

        if energy > 0:
            endTime = time.time()
            elapsedTime = int(endTime - startTime) + 1
        if elapsedTime >= 2:
            energy -= 1
            startTime = time.time()

        if energy >= 100:
            energyBar.shape(energyBarShape[10])
        elif energy >= 90:
            energyBar.shape(energyBarShape[9])
        elif energy >= 80:
            energyBar.shape(energyBarShape[8])
        elif energy >= 70:
            energyBar.shape(energyBarShape[7])
        elif energy >= 60:
            energyBar.shape(energyBarShape[6])
        elif energy >= 50:
            energyBar.shape(energyBarShape[5])
        elif energy >= 40:
            energyBar.shape(energyBarShape[4])
        elif energy >= 30:
            energyBar.shape(energyBarShape[3])
        elif energy >= 20:
            energyBar.shape(energyBarShape[2])
        elif energy >= 10:
            energyBar.shape(energyBarShape[1])
        elif energy <= 0:
            energyBar.shape(energyBarShape[0])
    def Obstacles():
        global difficulty

        xCorUpdated = [randint(-240, 0), randint(0, 150), randint(-200, 200), randint(-240, 240),
                       randint(-240, 0), randint(-240, 0)]
        yCorUpdated = [randint(100, 350), randint(100, 350)]

        def resetObstaclesPositions():
            asteroid0.goto(xCorUpdated[0], 550)
            asteroid0.shape(asteroidShapes[randint(0, 7)])
            asteroid1.goto(xCorUpdated[1], 750)
            asteroid1.shape(asteroidShapes[randint(0, 7)])
            if difficulty >= 3:
                asteroid2.goto(xCorUpdated[2], 950)
                asteroid2.shape(asteroidShapes[randint(0, 7)])
            if difficulty >= 4:
                asteroid3.goto(-350, yCorUpdated[0])
                asteroid3.shape(asteroidShapes[randint(0, 7)])
                asteroid4.goto(350, yCorUpdated[1])
                asteroid4.shape(asteroidShapes[randint(0, 7)])
            energyRefil.goto(xCorUpdated[3], 400)
            energyRefil.shape(energyShapes[randint(0, 3)])
        def hitORdie(reason):
            if reason == "Asteroid":
                if energy <= 0:
                    mixer.music.pause()
                    asteroidDie = mixer.Sound("Songs/OnGame/Asteroid/AsteroidDie.wav")
                    asteroidDie.play()
                    time.sleep(1.5)
                else:
                    mixer.music.pause()
                    asteroidHit = mixer.Sound("Songs/OnGame/Asteroid/AsteroidHit.wav")
                    asteroidHit.play()
                    time.sleep(0.75)
                    turtle.clear()
                    pauseGame()
            elif reason == "Wall":
                if energy <= 0:
                    mixer.music.pause()
                    wallDie = mixer.Sound("Songs/OnGame/Wall/WallDie.wav")
                    wallDie.play()
                    time.sleep(2)
                elif energy > 0:
                    mixer.music.pause()
                    wallHit = mixer.Sound("Songs/OnGame/Wall/WallHit.wav")
                    wallHit.play()
                    time.sleep(1)
                    turtle.clear()
                    pauseGame()

        def obstacleAsteroid0():
            if sqrt((player.xcor() - asteroid0.xcor())**2 + (player.ycor() - asteroid0.ycor())**2) <= 50:
                resetObstaclesPositions()
                spaceshipEnergy(0, 20)
                Panel(0, 10)
                player.goto(0, -200)
                hitORdie("Asteroid")

            elif asteroid0.ycor() >= -425:
                asteroid0.sety(asteroid0.ycor() - 7 - (2 * difficulty))

            elif asteroid0.ycor() <= -425:
                asteroid0.shape(asteroidShapes[randint(0, 7)])
                asteroid0.goto(xCorUpdated[0], 375)
                Panel(20, 0)
        def obstacleAsteroid1():
            if sqrt((player.xcor() - asteroid1.xcor())**2 + (player.ycor() - asteroid1.ycor())**2) <= 50:
                resetObstaclesPositions()
                spaceshipEnergy(0, 20)
                Panel(0, 10)
                player.goto(0, -200)
                hitORdie("Asteroid")

            elif asteroid1.ycor() >= -425:
                asteroid1.sety(asteroid1.ycor() - 5 - (2 * difficulty))

            elif asteroid1.ycor() <= -425:
                asteroid1.shape(asteroidShapes[randint(0, 7)])
                asteroid1.goto(xCorUpdated[1], 375)
                Panel(20, 0)
        def obstacleAsteroid2():
            if sqrt((player.xcor() - asteroid2.xcor())**2 + (player.ycor() - asteroid2.ycor())**2) <= 50:
                resetObstaclesPositions()
                spaceshipEnergy(0, 20)
                Panel(0, 10)
                player.goto(0, -200)
                hitORdie("Asteroid")

            elif asteroid2.ycor() >= -425:
                asteroid2.sety(asteroid2.ycor() - 8 - difficulty)
                if player.xcor() < 0 and asteroid2.xcor() < 0 and\
                        sqrt((player.xcor() - asteroid2.xcor()) ** 2 + (player.ycor() - asteroid2.ycor()) ** 2) <= 300:
                    asteroid2.setx(asteroid2.xcor() + 6)
                if player.xcor() > 0 and asteroid2.xcor() > 0 and\
                        sqrt((player.xcor() - asteroid2.xcor()) ** 2 + (player.ycor() - asteroid2.ycor()) ** 2) <= 300:
                    asteroid2.setx(asteroid2.xcor() - 6)

            elif asteroid2.ycor() <= -425:
                asteroid2.shape(asteroidShapes[randint(0, 7)])
                asteroid2.goto(xCorUpdated[2], 375)
                Panel(20, 0)
        def obstacleAsteroid3():
            if sqrt((player.xcor() - asteroid3.xcor())**2 + (player.ycor() - asteroid3.ycor())**2) <= 50:
                resetObstaclesPositions()
                spaceshipEnergy(0, 20)
                Panel(0, 10)
                player.goto(0, -200)
                hitORdie("Asteroid")

            elif asteroid3.xcor() >= -350:
                match difficulty:
                    case 4:
                        asteroid3.setx(asteroid3.xcor() + 4)
                        asteroid3.sety(asteroid3.ycor() - 6)
                    case 5:
                        asteroid3.setx(asteroid3.xcor() + 9)
                        asteroid3.sety(asteroid3.ycor() - 11)


            if asteroid3.xcor() >= 350:
                asteroid3.shape(asteroidShapes[randint(0, 7)])
                asteroid3.goto(-350, yCorUpdated[0])
                Panel(20, 0)
        def obstacleAsteroid4():
            if sqrt((player.xcor() - asteroid4.xcor())**2 + (player.ycor() - asteroid4.ycor())**2) <= 50:
                resetObstaclesPositions()
                spaceshipEnergy(0, 20)
                Panel(0, 10)
                player.goto(0, -200)
                hitORdie("Asteroid")

            elif asteroid4.xcor() <= 350:
                match difficulty:
                    case 4:
                        asteroid4.setx(asteroid4.xcor() - 4)
                        asteroid4.sety(asteroid4.ycor() - 6)
                    case 5:
                        asteroid4.setx(asteroid4.xcor() - 9)
                        asteroid4.sety(asteroid4.ycor() - 11)

            if asteroid4.xcor() <= -350:
                asteroid4.shape(asteroidShapes[randint(0, 7)])
                asteroid4.goto(350, yCorUpdated[1])
                Panel(20, 0)
        def obstacleEnergyRefil():
            if sqrt((player.xcor() - energyRefil.xcor())**2 + (player.ycor() - energyRefil.ycor())**2) <= 50:
                energyRefil.goto(xCorUpdated[3], 375)
                energyRefil.shape(energyShapes[randint(0, 3)])
                Panel(20, 0)
                gotEnergy = mixer.Sound("Songs/OnGame/Energy/GotEnergy.wav")
                gotEnergy.play()
                if energy < 100:
                    spaceshipEnergy(20, 0)

            elif energyRefil.ycor() >= -425:
                energyRefil.sety(energyRefil.ycor() - 4 - (2 * difficulty))

            elif energyRefil.ycor() <= -425:
                energyRefil.shape(energyShapes[randint(0, 3)])
                energyRefil.goto(xCorUpdated[2], 375)
        def Walls():
            if player.xcor() <= -240 or player.xcor() >= 240 or\
                    player.ycor() >= 370 or player.ycor() <= -380:
                resetObstaclesPositions()
                energyRefil.goto(xCorUpdated[3], 300)
                energyRefil.shape(energyShapes[randint(0, 3)])
                spaceshipEnergy(0, 20)
                Panel(0, 10)
                player.goto(0, -200)
                hitORdie("Wall")

        obstacleAsteroid0()
        obstacleAsteroid1()

        if difficulty >= 3:
            obstacleAsteroid2()
        if difficulty >= 4:
            obstacleAsteroid3()
            obstacleAsteroid4()
        obstacleEnergyRefil()
        Walls()

        screen.update()

    def pauseGame():
        global energy
        while energy > 0:
            mixer.music.pause()

            Writer(4, "PAUSE", "white", True)
            Writer(7, "\n\nPress Space to continue", "white", False)

            turtle.onkey(runGame, "Return")
            turtle.onkey(runGame, "space")
            turtle.onkey(runGame, "Escape")
            turtle.update()
            turtle.listen()
            turtle.clear()

            if difficulty == 0 and sqrt((player.xcor() - energyBar.xcor())**2 + (player.ycor() - energyBar.ycor())**2) <= 50:
                energy -= 1000
                eggSound = mixer.Sound("Songs/OnGame/Egg.wav")
                eggSound.play()
                time.sleep(1)
            elif difficulty >= 1:
                player.goto(0, -200)
    def runGame():
        while energy > 0:
            mixer.music.unpause()
            turtle.clear()

            turtle.goto(-175, 230)
            turtle.write(score, True, align='center', font=("Anticode", 20, "normal"))
            Writer(0, "SCORE", "white", True)

            turtle.goto(0, 230)
            turtle.write(difficulty, True, align='center', font=("Anticode", 20, "normal"))
            Writer(1, "Level", "white", True)

            Writer(2, "Energy", "white", True)
            screen.ontimer(Obstacles, 1000 // 60)
            spaceshipEnergy(0, 0)
            runningBackground()
            Panel(0, 0)

            turtle.onkey(pauseGame, "Escape")
            turtle.onkey(pauseGame, "space")

        if energy == 0:
            timeDie = mixer.Sound("Songs/OnGame/TimeDie.wav")
            timeDie.play(2)
            time.sleep(1.5)
            gameOver()
        elif energy <= -100:
            EGG()
        elif energy <= 0:
            gameOver()
    def gameOver():
        screen.title("Game Over.")
        screen.clearscreen()
        screen.bgcolor("black")
        screen.tracer(0, 0)

        mixer.stop()
        mixer.music.load("Songs/OnGame/GameOver.wav")
        mixer.music.play(-1)

        background = turtle.Turtle()
        background.shape("Images/Backgrounds/starfieldBackground4.gif")

        Writer(1, "GAME OVER", "white", True)
        Writer(4, f"Your score: {score}", "white", True)
        Writer(7, "Press SPACE to try again or ESC to exit.", "white", False)

        turtle.onkey(Exit, "Escape")
        turtle.onkey(Menu, "space")

        screen.update()

    ###################################
    def EGG():
        screen.title("Egg!!")
        screen.clearscreen()
        screen.bgcolor("black")
        screen.tracer(0, 0)

        spaceshipsShapes = ["Images/OnGame/Spaceships/spaceShip4.gif", "Images/OnGame/Spaceships/spaceShip5.gif",
                            "Images/OnGame/Spaceships/spaceShip6.gif"]
        background = turtle.Turtle()
        background.shape("Images/Menu/Egg.gif")

        mixer.music.load("Songs/OnGame/Megalovania.mp3")
        mixer.music.play(-1)

        def loadObstacles():
            obstacle0 = turtle.Turtle()
            time.sleep(0.2)
            obstacle0.penup()
            obstacle0.goto(-220, -50)
            obstacle0.shape(asteroidShapes[0])
            screen.update()

            obstacle1 = turtle.Turtle()
            time.sleep(0.2)
            obstacle1.penup()
            obstacle1.goto(220, -50)
            obstacle1.shape(asteroidShapes[3])
            screen.update()

            obstacle2 = turtle.Turtle()
            time.sleep(0.2)
            obstacle2.penup()
            obstacle2.goto(-220, 80)
            obstacle2.shape(asteroidShapes[5])
            screen.update()

            obstacle3 = turtle.Turtle()
            time.sleep(0.2)
            obstacle3.penup()
            obstacle3.goto(220, 80)
            obstacle3.shape(asteroidShapes[7])
            screen.update()
        def loadEnergies():
            energy0 = turtle.Turtle()
            time.sleep(0.2)
            energy0.penup()
            energy0.goto(100, -50)
            energy0.shape(energyShapes[0])
            screen.update()

            energy1 = turtle.Turtle()
            time.sleep(0.2)
            energy1.penup()
            energy1.goto(-100, -50)
            energy1.shape(energyShapes[1])
            screen.update()

            energy2 = turtle.Turtle()
            time.sleep(0.2)
            energy2.penup()
            energy2.goto(100, 80)
            energy2.shape(energyShapes[2])
            screen.update()

            energy3 = turtle.Turtle()
            time.sleep(0.2)
            energy3.penup()
            energy3.goto(-100, 80)
            energy3.shape(energyShapes[3])
            screen.update()
        def loadSpaceships():
            spaceship0 = turtle.Turtle()
            time.sleep(0.2)
            spaceship0.penup()
            spaceship0.goto(-170, -150)
            spaceship0.shape(spaceshipsShapes[0])
            screen.update()

            spaceship1 = turtle.Turtle()
            time.sleep(0.2)
            spaceship1.penup()
            spaceship1.goto(0, -150)
            spaceship1.shape(spaceshipsShapes[1])
            screen.update()

            spaceship2 = turtle.Turtle()
            time.sleep(0.2)
            spaceship2.penup()
            spaceship2.goto(170, -150)
            spaceship2.shape(spaceshipsShapes[2])
            screen.update()

        turtle.penup()
        turtle.goto(0, 140)
        turtle.color("white")
        turtle.write("created by", True, align='center', font=("Glitch Inside", 18, "normal"))
        turtle.hideturtle()
        screen.update()

        loadObstacles()
        loadSpaceships()
        loadEnergies()

        time.sleep(0.5)
        turtle.goto(-10, 0)
        turtle.write("   R. Henrique Cardoso", True, align='center', font=("Glitch Inside", 24, "normal"))
        turtle.hideturtle()

        turtle.goto(0, -300)
        turtle.write("Press ESC or Enter to exit", True, align='center', font=("Glitch Inside", 12 , "normal"))
        screen.update()

        def closeProgram():
            exit()

        turtle.onkey(closeProgram, "Escape")
        turtle.onkey(closeProgram, "Return")
        turtle.listen()
    ###################################

    mixer.music.load("Songs/OnGame/RunningGame.mp3")
    mixer.music.play(-1)

    Background()
    Player()
    setObjectsOnBackground()
    runGame()

screen = turtle.Screen()
screen.setup(600, 700)

Images()
pygame.init()
Menu()
screen.mainloop()