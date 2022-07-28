from tkinter import *
from time import *
from math import *
from random import *

root = Tk()
s = Canvas(root, width=800, height=600, background= "white")

#Importing images
def importImages():
	global bunnyA, bunnyB, easteregg, grass, bunnyEndA, bunnyEndB, bunnyStartA, bunnyStartB

	#Import start screen bunny images
	bunnyStartA = PhotoImage(file = "bunnyStart1.png")
	bunnyStartB = PhotoImage(file = "bunnyStart2.png")

	#Import game play bunny images 
	bunnyA = PhotoImage(file = "bunny.png")
	bunnyB = PhotoImage(file = "bunny.png")
	
	#Import easter egg image
	easteregg = PhotoImage(file = "easteregg.png")

	#Import grass image
	grass = PhotoImage(file = "grass.png")

	#Import end screen bunny images
	bunnyEndA = PhotoImage(file = "bunnyEnd1.png")
	bunnyEndB = PhotoImage(file = "bunnyEnd2.png")

def setInitialValues():
	global xBunny1, yBunny1, xBunny2, yBunny2, xSpeed1, ySpeed1, xSpeed2, ySpeed2, bunnyAbleToMove
	global numStream, streamx, streamy, length, width, streamxSpeed, streamColour, riverDrawing
	global egg, eggSpeeds, eggxPos, eggyPos, eggSpeed1, eggSpeed2 
	global point1, point2
	global startTime, countdownTime, clockDrawing
	
	#Bunny variables
	xBunny1 = 50
	yBunny1 = 150
	xBunny2 = 50
	yBunny2 = 450
	xSpeed1 = 0
	ySpeed1 = 0
	xSpeed2 = 0
	ySpeed2 = 0

	bunnyAbleToMove = False

	#Stream arrays
	numStream = 150
	streamx = []
	streamy = []
	length = []
	width = []
	streamxSpeed = []
	streamColour = []
	riverDrawing = []

	#Easter egg arrays
	egg = []
	eggSpeeds = []
	eggxPos = []
	eggyPos = []

	#Countdown variables
	startTime = time()
	countdownTime = 4
	clockDrawing = 0

	#Score variables
	point1 = 0
	point2 = 0

	importImages()
	fillArrayStream()
	fillArrayEasterEgg()

def keyHandler(event):
	global xSpeed1, ySpeed1, xSpeed2, ySpeed2, bunnyAbleToMove

	if bunnyAbleToMove == True: 
		#Keys for Bunny1	
		if event.keysym == "Left":
			xSpeed1 = -5

		elif event.keysym == "Right":
			xSpeed1 = 5

		elif event.keysym == "Up":
			ySpeed1 = -5

		elif event.keysym == "Down":
			ySpeed1 = 5

		#Keys for Bunny2
		if event.keysym == "a":
			xSpeed2 = -5

		elif event.keysym == "d":
			xSpeed2 = 5

		elif event.keysym == "w":
			ySpeed2 = -5

		elif event.keysym == "s":
			ySpeed2 = 5

#Stops when keys are released 
def keyUpHandler( event ):
	global xSpeed1, ySpeed1, xSpeed2, ySpeed2

	xSpeed1 = 0
	ySpeed1= 0

	xSpeed2 = 0
	ySpeed2 = 0


#============== Start Screen =======================
#Start screen backround
def startScreen():
	importImages()

	s.create_rectangle(0, 0, 800, 600, fill = "#74ccf4")

	s.create_rectangle(0, 350, 800, 600, fill = "#79d021", outline = "")
	
	#Mountains
	s.create_polygon(-100, 350, 150, 100, 350, 220, 420, 175, 525, 275, 650, 170, 900, 350, fill = "grey70"  )

	s.create_polygon(150, 100, 175, 175, 215, 180, 230, 270, 180, 350, 350, 220, 150, 100, fill = "grey90")
	s.create_polygon(420, 175, 400, 220, 450, 250, 440, 275, 590, 350, 525, 275,420, 175, fill = "grey90")
	s.create_polygon(650, 170, 630, 220, 675, 250, 665, 290, 900, 350, 650, 170, fill = "grey90")

	s.create_polygon(-100, 350, 150, 550, 350, 450, 420, 475, 525, 425, 650, 520, 900, 350, fill = "olive drab"  )

	#Clouds
	for i in range(0,20):
		xCloud = randint(0,800)
		yCloud = randint(-20,150)
		width = randint(60,90)
		height = randint(20,50)

		for i in range(0,10):
			xCloud1 = xCloud - randint(1, width)
			yCloud1 = yCloud - randint(1, height)
			xCloud2 = xCloud + randint(1, width)
			yCloud2 = yCloud + randint(1, height)
			s.create_oval( xCloud1, yCloud1, xCloud2, yCloud2, fill = "white", outline = "" )
	
	#Bunnies
	s.create_image(80, 470, image = bunnyStartA)
	s.create_image(720, 470, image = bunnyStartB)
	
	#Title
	s.create_text(400, 70, text = "Bunny Racer" , font = "Courier 48 bold", fill = "black" )

	#Easy button
	s.create_rectangle(300, 150, 500, 225, fill = "#0b0b45", outline = "")
	s.create_text(400, 187.5, text = "Easy" , font = "Arial 24 bold", fill = "white" )

	#Normal button
	s.create_rectangle(300, 235, 500, 310, fill = "#0b0b45", outline = "")
	s.create_text(400, 272.5, text = "Normal" , font = "Arial 24 bold", fill = "white")

	#Hard button
	s.create_rectangle(300, 320, 500, 395, fill = "#0b0b45", outline = "")
	s.create_text(400, 357.5, text = "Hard" , font = "Arial 24 bold", fill = "white" )

	#Instructions
	s.create_text(400, 520, text = "Dodge the easter eggs!" , font = "Arial 15 bold", fill = "white" )
	s.create_text(400, 555, text = "The player to finish 3 labs wins the game!" , font = "Arial 12 bold", fill = "white" )

	root.bind("<Button-1>", startScreenClick) #for when one of the buttons are clicked

def startScreenClick(event):
	global numEgg, a, b, c, d

	xMouse = event.x
	yMouse = event.y

	#when easy button is clicked (slow and less eggs)
	if 300 <= xMouse <= 500 and 150 <= yMouse <= 225:
		numEgg = 12
		a = 3
		b = 7
		c = -7
		d = -3
		runGame()

	#when normal button is clicked
	elif 300 <= xMouse <= 500 and 235 <= yMouse <= 310:
		numEgg = 18
		a = 4
		b = 8
		c = -8
		d = -4
		runGame()

	#when hard button is clicked (fast and more eggs)
	elif 300 <= xMouse <= 500 and 320 <= yMouse <= 395:
		numEgg = 25
		a = 4
		b = 9
		c = -9
		d = -4
		runGame()
	
	else:
		pass

		
#=============== Backround in Game Play ===========================
def drawBackround(): 

	s.create_rectangle(0, 0, 800, 600, fill = "#79d021")

	#Grass
	for n in range(2500):
		xGrass = randint(0,800)
		yGrass = randint(0,600)

		slant = uniform(-2,10)
		grassShade = randint(1,4)
		grassCol = "DarkOliveGreen" + str(grassShade)

		s.create_line( xGrass, yGrass, xGrass + 3, yGrass + slant, fill = grassCol )

	#Finish line
	s.create_line(780, 0, 780, 800, width = 3, fill = "white")

	#Stream
	s.create_rectangle(0, 275, 800, 325, fill = "#38afcd", outline = "")

	#Stones
	for i in range(200):
		spacing = 7 * i		

		stoneSize = randint(4,7)
		stoneShade = randint(20,80)
		stoneCol = "grey" + str(stoneShade)

		s.create_oval( spacing - stoneSize, 325 - stoneSize, spacing + stoneSize, 325 + stoneSize, fill = stoneCol, outline = "")
		s.create_oval( spacing - stoneSize, 275 - stoneSize, spacing + stoneSize, 275 + stoneSize, fill = stoneCol, outline = "")

#Fill empty arrays for the stream
def fillArrayStream():
	global numStream, streamx, streamy, length, width, streamxSpeed, streamColour, riverDrawing

	for i in range(numStream):
		streamx.append(randint(-200,800))
		streamy.append(randint(285,315))
		length.append(randint(30,70))
		width.append(randint(1,3))
		streamxSpeed.append(randint(2,7))
		streamColour.append(choice(["#0f5e9c", "#2389da","#1ca3ec", "#5abcd8", "#74ccf4"]))
		riverDrawing.append(0)

#Stream animation
def drawStream():
	global numStream, streamx, streamy, length, width, streamxSpeed, streamColour, riverDrawing

	for i in range(numStream):
		riverDrawing[i] = s.create_line(streamx[i], streamy[i], streamx[i] + length[i], streamy[i], fill = streamColour[i], width = width[i])

		streamx[i] = streamx[i] + streamxSpeed[i]

		if streamx[i] > 800:
			streamx[i] = -200


#===========Bunny Procedures===============

#Gets called in every frame. Updates the position of the bunnies in current frame
def updateBunnyPosition():
	global xBunny1, yBunny1, xBunny2, yBunny2

	xBunny1 = xBunny1 + xSpeed1
	yBunny1 = yBunny1 + ySpeed1

	xBunny2 = xBunny2 + xSpeed2
	yBunny2 = yBunny2 + ySpeed2

	#Prevents Bunny1 from going out of its area
	if xBunny1 < 0: 
		xBunny1 = 0

	if xBunny1 > 780: # when reached finish line, goes back to staring point
		xBunny1 = 50

	if yBunny1 < 0: 
		yBunny1 = 0

	if yBunny1 > 250: 
		yBunny1 = 250

	#Prevents Bunny2 from going out of its area
	if xBunny2 < 0: 
		xBunny2 = 0

	if xBunny2 > 780: # when reached finish line, goes back to staring point
		xBunny2 = 50

	if yBunny2 < 350: 
		yBunny2 = 350

	if yBunny2 > 600: 
		yBunny2 = 600

#Inserting Bunnies
def drawBunny():
	global bunny1, bunny2

	bunny1 = s.create_image(xBunny1, yBunny1, image = bunnyA )
	bunny2 = s.create_image(xBunny2, yBunny2, image = bunnyB )


#============= Easter Egg Procedures ================

#Fill empty arrays for easter eggs
def fillArrayEasterEgg():
	global egg, eggSpeeds, eggxPos, eggyPos, numEgg

	for i in range(numEgg):
		eggxPos.append(randint(130, 750))
		eggyPos.append(choice([-10, 610])) #comes out either at the top or bottom

		if eggyPos[len(eggyPos)-1] == -10: #if the eggs comes out from the top, it gets a random speed
			eggSpeeds.append(uniform(a, b)) 

		else:
			eggSpeeds.append(uniform(c, d)) #if the eggs comes out from the bottom, it gets a random speed

		egg.append(0)

def moveEgg():
	global numEgg, egg, eggSpeeds, eggxPos, eggyPos

	for i in range(numEgg):
		eggyPos[i] = eggyPos[i] + eggSpeeds[i]
		egg[i] = s.create_image(eggxPos[i],eggyPos[i], image = easteregg)

		if eggyPos[i] < -10: #if the egg reaches the top, it goes back to the bottom
			eggyPos[i] = 610
			eggxPos[i] = randint(130, 750)

		if eggyPos[i] > 610: #if the egg reaches the bottom, it goes back to the top
			eggyPos[i] = -10
			eggxPos[i] = randint(130, 750)

def eggCollision():
	global xBunny1, yBunny1, xBunny2, yBunny2
	global eggxPos, eggyPos

	for i in range(numEgg):
		#the distance between the eggs and bunnies
		distance1 = sqrt( (xBunny1-eggxPos[i])**2 + (yBunny1-eggyPos[i])**2 )
		distance2 = sqrt( (xBunny2-eggxPos[i])**2 + (yBunny2-eggyPos[i])**2 )

    #When a bunny gets hit by a egg
		#If the distance between the egg and bunnny is less than 30, the bunny goes back to the start point
		if distance1 <= 30: 
			xBunny1 = 50

		if distance2 <= 30:
			xBunny2 = 50


#================= Countdown =========================
def countdown():
	global startTime, countdownTime, clockDrawing, bunnyAbleToMove

	#3, 2, 1 countdown before beginning the game
	timeSinceLastTick = time() - startTime

	if timeSinceLastTick >= 1:
		s.delete(clockDrawing)
		countdownTime = countdownTime - 1
		startTime = time()

		if countdownTime == 0: 
			clockDrawing = s.create_text(400, 450, text = "Go!", font = "Arial 80 bold", fill = "white")
			bunnyAbleToMove = True
	
		elif countdownTime > 0:
			clockDrawing = s.create_text(400, 150, text = countdownTime, font = "Arial 80 bold", fill = "white")


#=================== Score ============================
def score():
	global score1, score2, point1, point2

	#When the bunnies reach the finish line, it gains a point
	if xBunny1 == 780:
		point1 = point1 + 1

	score1 = s.create_text(50, 150, text = point1, font = "Arial 80 bold", fill = "white")
	
	if xBunny2 == 780:
		point2 = point2 + 1

	score2 = s.create_text(50, 450, text = point2, font = "Arial 80 bold", fill = "white")

#The player that get 3 points(3 laps) first win the game
def winner():
	global point1, point2

	if point1 == point2 == 3: 
		s.create_text(450, 150, text = "It's a" , font = "Arial 80 bold", fill = "white") 
		s.create_text(450, 450, text = "Draw!" , font = "Arial 80 bold", fill = "white")

	elif point1 == 3: 
		s.create_text(450, 150, text = "You Win!" , font = "Arial 80 bold", fill = "white") 

	elif point2 == 3: 
		s.create_text(450, 450, text = "You Win!" , font = "Arial 80 bold", fill = "white")
	

#============= Ending Screen ================================
#End screen backround
def endGame():
	global endScreenSky, endScreenC, mount1, mount2, mount3, mount4, mount5, clouds, BunnyEnd1, BunnyEnd2, endStream, endGrass, endBox, endText

	endScreenSky = s.create_rectangle(0, 0, 800, 600, fill = "#74ccf4")
	endScreenC = s.create_rectangle(0, 300, 800, 600, fill = "#79d021", outline = "")

	#Mountains
	mount1 = s.create_polygon(-100,300,150,50,350,170,420,125, 525,225, 650, 120, 900,300, fill = "grey70" )

	mount2 = s.create_polygon(150,50,175,125,215,130,230,220,180,300,350,170, 150, 50, fill = "grey90")
	mount3 = s.create_polygon(420,125,400,170,450,200,440,225,590,300,525,225,420,125, fill = "grey90")
	mount4 = s.create_polygon(650,120,630,170,675,200,665,240,900,300,650,120, fill = "grey90")

	mount5 = s.create_polygon(-100,300,150,500,350,400,420,425, 525,375,650, 470, 900, 300, fill = "olive drab"  )

	#Clouds
	for i in range(0,20):
		xCloud = randint(0,800)
		yCloud = randint(-20, 75)
		width = randint(60,90)
		height = randint(20,50)

		for i in range(0,7):
			xCloud1 = xCloud - randint(1, width)
			yCloud1 = yCloud - randint(1, height)
			xCloud2 = xCloud + randint(1, width)
			yCloud2 = yCloud + randint(1, height)
			clouds = s.create_oval( xCloud1, yCloud1, xCloud2, yCloud2, fill = "white", outline = "" )

	#Bunnies
	BunnyEnd1 = s.create_image(100, 300, image = bunnyEndA)
	BunnyEnd2 = s.create_image(700, 300, image = bunnyEndB)

	endStream = s.create_rectangle(0, 500, 800, 600, fill = "#38afcd")
	endGrass = s.create_image(400, 400, image = grass )

	#Box and text for "Play Again"
	endBox = s.create_rectangle(250, 50, 550, 150, fill = "#0b0b45", outline = "")
	endText = s.create_text(400, 100, text = "Play Again" , font = "Arial 24 bold", fill = "white" )

	root.bind("<Button-1>", endGameClick) #for when "play again" is clicked

#Detects clicks for end game screen
def endGameClick(event):
		xMouse = event.x
		yMouse = event.y

		if 250 <= xMouse <= 550 and 50 <= yMouse <= 150:
			s.delete(endScreenSky, endScreenC, mount1, mount2, mount3, mount4, mount5, clouds, BunnyEnd1, BunnyEnd2, endStream, endGrass, endBox, endText)
			startScreen()


#========================= Main Loop (Running The Game) =========================
def runGame():
	global point1, point2

	setInitialValues()
	drawBackround()

	while point1 < 3 and point2 < 3: # runs the game until  player gets 3 points
		countdown()	
		score()

		updateBunnyPosition()
		drawBunny()
		drawStream()
		moveEgg()
		eggCollision()

		winner()

		s.update()
		sleep(0.03)
		s.delete(bunny1, bunny2, score1, score2 )

		for i in range(numStream): #delete stream 
			 s.delete(riverDrawing[i])

		for i in range(numEgg): #delete eggs 
			s.delete(egg[i])

	sleep(2)
	endGame()

root.after(0, startScreen())

#Bindings
s.bind( "<Key>", keyHandler) #This handles any key the user pushes
s.bind("<KeyRelease>", keyUpHandler)  #This handles things whenever the user lets go of any key

s.pack()
s.focus_set()
root.mainloop()
