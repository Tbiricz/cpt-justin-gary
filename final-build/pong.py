x = 250
y = 250
w = 50
h = 50
speedX = 5
speedY = 4
paddleW = 30
paddleH = 100
paddleS = 10
keyStatesL = []
keyStatesR = []
screen = 3
contSize = 40
score1, score2 = 0, 0
playSize = 30
htpSize = 30
backSize = 20
textY = 100
textS = 2
colour1 = color(0, 0, 0)
colour2 = color(0, 0, 0)
timeAccessed = None
for i in range(233):
    keyStatesR.append(False)
paddleR = PVector(485, 250)

for i in range(233):
    keyStatesL.append(False)
paddleL = PVector(15, 250)


def setup():
    size(500, 500)
    rectMode(CENTER)
    ellipseMode(CENTER)
    textMode(CENTER)


def draw():
    global keyStatesR
    global screen
    global htpSize
    global playSize

    if screen == 1:
        if keyStatesR[38]:  # up
            paddleR.y -= 5
        elif keyStatesR[40]:  # down
            paddleR.y += 5

        if keyStatesL[87]:
            paddleL.y -= 5
        elif keyStatesL[83]:
            paddleL.y += 5

        background(0)

        drawBall()
        drawPaddle()
        moveBall()
        bounceDirection()
        restrictPaddle()
        contactPaddle()
        drawScore()

    if screen == 2:
        global contSize

        background(0)

        textSize(contSize)

        if mouseX >= 160 and mouseX <= 340 and mouseY >= 260 and mouseY <= 300:
            fill(34, 139, 34)
            contSize = 50
            contX = 140
        else:
            fill(255, 0, 0)
            contSize = 40
            contX = 160
        text("Continue", contX, 300)

        if (mouseX >= 160 and mouseX <= 340 and mouseY >= 260 and
           mouseY <= 300 and mousePressed):
            screen = 1

    if screen == 3:
        global textY, textS
        global colour1, colour2

        background(0)

        if textY >= 100:
            textS = -textS
        elif textY <= 25:
            textS = -textS

        textY += textS

        textSize(50)
        fill(255)
        text("P  ng", 30, 100)

        fill(255, 0, 0)
        text("o", 59, textY)

        textSize(htpSize)
        fill(colour1)
        text("How to Play", 20, 200)

        if mouseX >= 20 and mouseX <= 250 and mouseY >= 170 and mouseY <= 200:
            htpSize = 40
            colour1 = color(255, 238, 0)
        else:
            htpSize = 30
            colour1 = color(21, 255, 0)

        if (mouseX >= 20 and mouseX <= 250 and mouseY >= 170 and
           mouseY <= 200 and mousePressed):
            screen = 6

        textSize(playSize)
        fill(colour2)
        text("Play", 20, 250)

        if mouseX >= 20 and mouseX <= 150 and mouseY >= 220 and mouseY <= 250:
            playSize = 40
            colour2 = color(255, 238, 0)
        else:
            playSize = 30
            colour2 = color(21, 255, 0)

        if (mouseX >= 20 and mouseX <= 150 and mouseY >= 220 and
           mouseY <= 250 and mousePressed):
            screen = 5

    if screen == 4:
        fill(255, 0, 0, 70)
        rect(250, 250, 500, 500)

        fill(255)
        textSize(20)
        text("Click Anywhere to Continue", 110, 350)

        if (mouseX >= 0 and mouseX <= 500 and mouseY >= 0 and
           mouseY <= 500 and mousePressed):
            screen = 5

        drawBall()
        drawPaddle()
        drawScore()

    if screen == 5:
        import time
        global timeAccessed

        timeAccessed = timeAccessed or millis()

        background(0)

        drawBall()
        drawPaddle()
        drawScore()

        fill(255)
        textSize(50)
        text("Ready?", 175, 265)

        if millis() > timeAccessed + 2000:
            timeAccessed = None
            screen = 1

    if screen == 6:
        global backSize

        background(0)

        textSize(20)
        fill(255)
        text("Player 1: W - Up, S - Down", 20, 100)
        text("PLayer 2: ARROW KEYS - Up, Down", 20, 140)

        textSize(backSize)
        fill(255)
        text("BACK", 20, 470)

        if mouseX >= 20 and mouseX <= 150 and mouseY >= 440 and mouseY <= 470:
            backSize = 30
        else:
            backSize = 20

        if (mouseX >= 20 and mouseX <= 150 and mouseY >= 440 and
           mouseY <= 470 and mousePressed):
            screen = 3


def drawScore():
    textMode(CENTER)
    textSize(40)
    fill(255)
    text(score1, 150, 50)
    text(score2, 320, 50)


def drawBall():
    fill(255, 0, 0)
    ellipse(x, y, w, h)


def moveBall():
    global x
    global y

    x += speedX
    y += speedY


def bounceDirection():
    global speedX
    global speedY

    if x > width - w / 2:
        speedX = -speedX
    elif x < 0 + w / 2:
        speedX = -speedX

    if y > height - h / 2:
        speedY = -speedY
    elif y < 0 + h / 2:
        speedY = -speedY


def drawPaddle():
    fill(255, 238, 0)
    rect(paddleR.x, paddleR.y, paddleW, paddleH)

    fill(21, 255, 0)
    rect(paddleL.x, paddleL.y, paddleW, paddleH)


def restrictPaddle():
    global paddleS
    if paddleR.y - paddleH / 2 < 0:
        paddleR.y += 5
    if paddleR.y + paddleH / 2 > height:
        paddleR.y -= 5

    if paddleL.y - paddleH / 2 < 0:
        paddleL.y = paddleL.y + paddleS
    if paddleL.y + paddleH / 2 > height:
        paddleL.y = paddleL.y - paddleS


def contactPaddle():
    global speedX
    global screen
    global x
    global y
    global score1
    global score2

    # left paddle
    if x == 50 and y < paddleL.y + 70 and y > paddleL.y - 70:
        if speedX < 0:
            speedX = -speedX

    if x <= 25:
        screen = 4
        score2 += 1
        x = 250
        y = 250
        paddleL.y = 250
        paddleR.y = 250

    # right paddle
    if x == 450 and y < paddleR.y + 70 and y > paddleR.y - 70:
        if speedX > 0:
            speedX = -speedX

    if x >= 475:
        screen = 4
        score1 += 1
        x = 250
        y = 250
        paddleL.y = 250
        paddleR.y = 250


def keyPressed():
    global keyStatesR
    global keyStatesL
    keyStatesR[keyCode] = True
    keyStatesL[keyCode] = True


def keyReleased():
    global keyStatesR
    global keyStatesL
    keyStatesR[keyCode] = False
    keyStatesL[keyCode] = False
