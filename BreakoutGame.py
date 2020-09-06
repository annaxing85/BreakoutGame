from processing import *
import time
import random


def setup():
    frameRate(70)
    size(600, 400)
    noStroke()
    createBlocks()

################ Create Blocks ################ 
class Block:
  x = 0
  y = 0
  blockWidth = 50
  blockHeight = 15

blockList = []
def createBlocks():
    numBlocksPerRow = 10
    numBlocksPerColumn = 5
    blockSep = 10
    shiftX = width/2.0 - (numBlocksPerRow/2.0)*Block().blockWidth - ((numBlocksPerRow-1)/2.0 * blockSep);
    for row in range(numBlocksPerColumn):
        for column in range(numBlocksPerRow):
            xBrickCoordinate = shiftX+(Block().blockWidth*column + blockSep*column); 
            yBrickCoordinate = 29 + Block().blockHeight*row + blockSep*row;
            block = Block()
            block.x = xBrickCoordinate
            block.y = yBrickCoordinate
            blockList.append(block)

def drawBlock(): # Draws each block within the blockList
  if blockList == []: # Ends game when no more blocks
      print "gameover"
  fill(30, 100, 250)
  
  for block in blockList:
    rect(block.x, block.y, block.blockWidth, block.blockHeight)
    
################################################ 

# variableS
paddle_x = 250
paddle_y = 370
paddle_width = 80
paddle_height = 20

ball_x = 300
ball_y = 200
ball_size = 20

speed_x=-6
speed_y=8

score=0

lives=3

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

gameover=False

def drawPaddle():
    # move paddle
    global paddle_x
    paddle_x = mouseX

    # draw paddle
    paddle_color = color(0, 0, 0)
    fill(paddle_color)
    rect(paddle_x, paddle_y, paddle_width, paddle_height)
    

def drawBall():  
    #move ball, TODO
    global ball_x, ball_y
    ball_x=ball_x + speed_x
    ball_y=ball_y + speed_y
    ball_color = color(0, 200, 0)
    fill(ball_color)
    ellipse(ball_x, ball_y, ball_size, ball_size)
    
def bounceOffWalls():
  global speed_x, speed_y
  #left 
  if ball_x < 0:
    speed_x= -speed_x
    
    
  #right
  if ball_x > 600:
    speed_x= -speed_x
    
    
  #top
  if ball_y < 0:
    speed_y= -speed_y
   
    
  
    
def ballInPaddle():
  global speed_y
  topleft=pointInRect(ball_x, ball_y, paddle_x, paddle_y, paddle_width, paddle_height)
  topright=pointInRect(ball_x+ball_size, ball_y, paddle_x, paddle_y, paddle_width, paddle_height)
  bottomleft=pointInRect(ball_x, ball_y+ball_size, paddle_x, paddle_y, paddle_width, paddle_height)
  bottomright=pointInRect(ball_x+ball_size, ball_y+ball_size, paddle_x, paddle_y, paddle_width, paddle_height)
  if topleft or topright or bottomleft or bottomright:
    speed_y= -abs(speed_y)
  

def pointInRect(pt_x, pt_y, x, y, w, h): 
  if (pt_x > x) and (pt_x < x + w) and (pt_y > y) and (pt_y < y + h): 
    return True 
  else:
    return False
  
def hitBrick():
  global speed_y
  for block in blockList:
    topleft=pointInRect(ball_x, ball_y, block.x, block.y, block.blockWidth, block.blockHeight)
    topright=pointInRect(ball_x+ball_size, ball_y, block.x, block.y, block.blockWidth, block.blockHeight)
    bottomleft=pointInRect(ball_x, ball_y+ball_size, block.x, block.y, block.blockWidth, block.blockHeight)
    bottomright=pointInRect(ball_x+ball_size, ball_y+ball_size, block.x, block.y, block.blockWidth, block.blockHeight)
    if topleft or topright or bottomleft or bottomright:
      blockList.remove(block)
      speed_y= -speed_y
      addscore()
    
    
def drawscore():
  textSize(20)
  fill(0,0,0)
  text("Score: " + str(score),400,20)

def addscore():
  global score
  score=score + 1
  
def threelives():
  global ball_x, ball_y, lives
  if ball_y > 400:
    ball_x = 300
    ball_y = 200
    lives=lives - 1
    checkscreen()
    
def checkscreen():
  global gameover
  if lives==0:
    gameover=True
    
    
def drawlives():
  textSize(20)
  fill(0,0,0)
  text("Lives: " + str(lives),500,20)


def draw():
  if gameover== False:
    bg_color = color(207,256,236)
    background(bg_color)
    drawBlock()
    drawPaddle()
    drawBall()
    bounceOffWalls()
    ballInPaddle()
    hitBrick()
    drawscore()
    threelives()
    drawlives()
  else:
    background(r,g,b)
    textSize(50)
    fill(0,0,0)
    text("GAME OVER",600/2-140,400/2)
    
run()