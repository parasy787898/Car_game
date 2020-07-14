import pygame
import random
from os import path
import shelve

pygame.init()
#used to initialize the pygame module.    

#Creating a window for our game.
app = pygame.display.set_mode((700, 700))

joystick = pygame.joystick.get_count()
if joystick == 0:
    # No joysticks!
    print("Game have found that no joystick is attached.")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

#Setting up the title of the window.
pygame.display.set_caption("Game")

#loading images form my storage location.

bg = pygame.image.load(path.join(path.dirname(__file__), "data","road.png"))
boom = pygame.image.load(path.join(path.dirname(__file__), "data","boom.png"))
tree = pygame.image.load(path.join(path.dirname(__file__), "data","tree.png"))
car_0 = pygame.image.load(path.join(path.dirname(__file__), "data","red.png"))
car_1 = pygame.image.load(path.join(path.dirname(__file__), "data","car1.png"))
car_2 = pygame.image.load(path.join(path.dirname(__file__), "data","car2.png"))
car_3 = pygame.image.load(path.join(path.dirname(__file__), "data","car3.png"))
car_4 = pygame.image.load(path.join(path.dirname(__file__), "data","car4.png"))
car_5 = pygame.image.load(path.join(path.dirname(__file__), "data","car5.png"))
strip = pygame.image.load(path.join(path.dirname(__file__), "data","strip.png"))
blue_car = pygame.image.load(path.join(path.dirname(__file__), "data","blue.png"))
white_car = pygame.image.load(path.join(path.dirname(__file__), "data","white.png"))
yellow_car = pygame.image.load(path.join(path.dirname(__file__), "data","yellow.png"))

#importing crash sound
crash = pygame.mixer.Sound(path.join(path.dirname(__file__), "data","crash.wav"))

# importing game's high scores.
high_score= path.join(path.dirname(__file__), "data","score")

try:
    score_file = shelve.open(high_score)   
    h_score  = score_file['score']         

except:
    score_file = shelve.open(high_score)   
    score_file['score']=0
    score_file.close()
    score_file =shelve.open(high_score)

class car_variable(object):
    def __init__(self):
        self.player_car = car_0 #default car

#Creating variables to move our car in window
x = 200
y = 600
speed = 2
score = -3
speed_inc=10
car_speed = 2  # Speed of random car with respect to frame.

#variables for the random/computer generated cars
#setting intial values for cars
a1 = 0
b1 = 233
c1 = 466
a = 500
b = 500
c = 500

#creating variables for road's strip
d = 345
d1 = 0
d2 = 100
d3 = 200
d4 = 300
d5 = 400
d6 = 500
d7 = 600

#Creating variables for tree
t = 25
tr = 635
t1 = 0
t2 = 115
t3 = 230
t4 = 345
t5 = 460
t6 = 575 

#defining a function for cars and background


def images():

  #Make sure first insert background.
  app.blit(bg, (0, 0))

  #Syntax= app.blit(image, variables to place image)

  #Inserting road stips
  app.blit(strip, (d, d1))
  app.blit(strip, (d, d2))
  app.blit(strip, (d, d3))
  app.blit(strip, (d, d4))
  app.blit(strip, (d, d5))
  app.blit(strip, (d, d6))
  app.blit(strip, (d, d7))

  #inserting Trees
  app.blit(tree, (t, t1))
  app.blit(tree, (tr, t2))
  app.blit(tree, (t, t3))
  app.blit(tree, (tr, t4))
  app.blit(tree, (t, t5))
  app.blit(tree, (tr, t6))

  #inserting images of car.
  app.blit(var.player_car, (x, y))
  app.blit(yellow_car, (a, a1))
  app.blit(blue_car, (c, c1))
  app.blit(white_car, (b, b1))

  #Creating the Score Board
  if score>=0:
    font = pygame.font.Font(None, 50)
    text = font.render("Score: "+str(score), 1, (255, 255, 255))
    app.blit(text, (55, 10))

  font = pygame.font.Font(None, 50)
  text = font.render("High Score: "+str(h_score), 1, (255, 255, 255))
  app.blit(text, (370, 10))


  pygame.display.update()
  #it is a function to update screen.
#-------------------------------------------------------

#The Case for Accident:
def accident(x, y):
  app.blit(boom, (x, y))
  pygame.display.update()
  pygame.time.delay(500)

#Game Over Screen
def game_over_screen():
  app.blit(bg, (0, 0))
  #game over Text
  font = pygame.font.Font(None, 75)
  text = font.render("Game Over", 1, (255, 255, 255))
  app.blit(text, (200, 100))

  if h_score<= score:
    font = pygame.font.Font(None, 50)
    text = font.render("New High Score: "+str(score), 1, (255, 255, 255))
    app.blit(text, (200, 250))

  else:
    font = pygame.font.Font(None, 50)
    text = font.render("Your score: "+str(score), 1, (255, 255, 255))
    app.blit(text, (230, 250))

  font = pygame.font.Font(None, 35)
  text = font.render("Press Space key to Restart", 1, (255, 255, 255))
  app.blit(text, (195, 400))

  text = font.render("Press Shift key to Choose Another Car", 1, (255, 255, 255))
  app.blit(text, (130, 450))

  pygame.display.update()

  waiting = True
  while waiting:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LSHIFT] or keys_pressed[pygame.K_RSHIFT]:
              choose_car_screen()

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
              waiting = False
            

#Function to choose car from the list
def choose_car_screen():
  waiting1 = True
  while waiting1:
    app.blit(bg, (0, 0))
    font = pygame.font.Font(None, 35)
    text = font.render("Tap on the car to choose then Space to start", 1, (255, 255, 255))
    app.blit(text, (92, 100))

    app.blit(car_0, (200, 200))
    app.blit(car_1, (200, 375))
    app.blit(car_2, (200, 550))
    app.blit(car_3, (450, 200))
    app.blit(car_4, (450, 375))
    app.blit(car_5, (450, 550))

    font = pygame.font.Font(None, 25)
    text = font.render("1.", 1, (255, 255, 255))
    app.blit(text, (185, 200))

    text = font.render("2.", 1, (255, 255, 255))
    app.blit(text, (185, 375))

    text = font.render("3.", 1, (255, 255, 255))
    app.blit(text, (185, 550))

    text = font.render("4.", 1, (255, 255, 255))
    app.blit(text, (435, 200))

    text = font.render("5.", 1, (255, 255, 255))
    app.blit(text, (435, 375))

    text = font.render("6.", 1, (255, 255, 255))
    app.blit(text, (435, 550))

    for event in pygame.mouse.get_pressed():
      x, y = pygame.mouse.get_pos()
      
      if x in range (200,250):
        if y in range (200,300):
            pygame.draw.rect(app,(0,0,0),(195,195,60,110) , 5)
            var.player_car=car_0

        if y in range (375,475):
            if h_score>30:
                pygame.draw.rect(app,(0,0,0),(195,370,60,110) , 5)
                var.player_car=car_1
            else:
                font = pygame.font.Font(None, 30)
                text = font.render("Your Highscore must be more than 30 to choose this car", 1, (255, 255, 255))
                app.blit(text, (70, 325))

        if y in range (550,650):
            if h_score>50:
                pygame.draw.rect(app,(0,0,0),(195,545,60,110) , 5)
                var.player_car=car_2
            else:
                font = pygame.font.Font(None, 30)
                text = font.render("Your Highscore must be more than 50 to choose this car", 1, (255, 255, 255))
                app.blit(text, (70, 325))

      if x in range (450,500):
        if y in range (200,300):
            if h_score>70:
                pygame.draw.rect(app,(0,0,0),(445,195,60,110) , 5)
                var.player_car=car_3
            else:
                font = pygame.font.Font(None, 30)
                text = font.render("Your Highscore must be more than 70 to choose this car", 1, (255, 255, 255))
                app.blit(text, (70, 325))

        
        if y in range (375,475):
            if h_score>100:
                pygame.draw.rect(app,(0,0,0),(445,370,60,110) , 5)
                var.player_car=car_4
            else:
                font = pygame.font.Font(None, 30)
                text = font.render("Your Highscore must be more than 100 to choose this car", 1, (255, 255, 255))
                app.blit(text, (70, 325))

        
        if y in range (550,650):
            if h_score>120:
                pygame.draw.rect(app,(0,0,0),(445,545,60,110) , 5)
                var.player_car=car_5
            else:
                font = pygame.font.Font(None, 30)
                text = font.render("Your Highscore must be more than 120 to choose this car", 1, (255, 255, 255))
                app.blit(text, (70, 325))


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()

      keys_pressed = pygame.key.get_pressed()
      if keys_pressed[pygame.K_SPACE]:
        waiting1 = False

    pygame.display.update()

#Game Start Screen
def game_Start_screen():
  app.blit(bg, (0, 0))
  #game over Text
  font = pygame.font.Font(None, 40)
  text = font.render("Welcome to car Game", 1, (255, 255, 255))
  app.blit(text, (200, 200))

  text = font.render("Press Space key to Start", 1, (255, 255, 255))
  app.blit(text, (190, 350))

  font = pygame.font.Font(None, 35)
  text = font.render("Press Shift key to Choose Another Car", 1, (255, 255, 255))
  app.blit(text, (130, 450))

  pygame.display.update()

  #loop to Wait For user until he presses Space Bar or Exit
  waiting1 = True
  while waiting1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LSHIFT] or keys_pressed[pygame.K_RSHIFT]:
              choose_car_screen()

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
              waiting1 = False

clock = pygame.time.Clock()
var= car_variable()

# The window closes after few time to stop that we need to make a loop.
runtime = True
game_over = False
start_game = True
while runtime:

   # creating a FPS lock for the game.
  clock.tick(60)

  # creating a Start screen for game
  if start_game:
    game_Start_screen()
    start_game = False

  #Game over Logic
  if game_over:

    if h_score<int(score):
      score_file['score'] = h_score = score
    score_file.close()
    score_file = shelve.open(high_score)

    if score<0:
      score=0

    game_over_screen() 
    game_over = False

    #Resetting everything on starting
    a1 = 0
    b1 = 233
    c1 = 466
    a = 548
    b = 548
    c = 548
    x = 200
    y = 600
    score = -3
    speed = 2
    car_speed=1
    
  # Creating a way to exit the program.
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      runtime = False

  #Assigning keys to control the movement of our square.
  keys_pressed = pygame.key.get_pressed()

  #Assigining right motion to right arrow
  if keys_pressed[pygame.K_RIGHT]:
    if x < 548:
      x = x +  (speed*2)

  #Assigining left motion to Left arrow
  if keys_pressed[pygame.K_LEFT]:
    if x > 103:
      x = x - (speed*2)

  #Assigining downward motion to down arrow
  if keys_pressed[pygame.K_DOWN]:
    if y < 600:
      y = y + (speed*2)

  #Assigining upward motion to up arrow
  if keys_pressed[pygame.K_UP]:
    if y > 0:
      y = y - (speed*2)

  if joystick != 0:
    # This gets the position of the axis on the game controller
    # It returns a number between -1.0 and +1.0
    horiz_axis_pos = joystick.get_axis(0)
    vert_axis_pos = joystick.get_axis(1)

    # Move x according to the axis and then multiply by current speed
    # for the movement.
    qw = int(horiz_axis_pos *2* speed)
    er = int(vert_axis_pos *2* speed)
    if qw < 0:
      if x >= 100:
        x = x + qw
    else:
      if x <= 550:
        x = x + qw

    if er < 0:
      if y >= 0:
        y = y + er
    else:
     if y <= 600:
      y = y + er

  # Increasing hardness with score:
  if score > speed_inc :
      speed = speed+1
      speed_inc = speed_inc*2

  #changing variables of random cars to make them move
  if a1 >= 700:
    a1 = -100  # Restarting car from starting position
    a = random.randint(103, 230)  # selecting random position of car in x axis
    score = score+1

  if c1 >= 700:
    c1 = -100
    c = random.randint(270, 360)
    score = score+1

  if b1 >= 700:
    b1 = -100
    b = random.randint(400, 545) 
    score = score+1

  #Restarting the strips
  if d1 >= 700:
    d1 = 0
  if d2 >= 700:
    d2 = 0
  if d3 >= 700:
    d3 = 0
  if d4 >= 700:
    d4 = 0
  if d5 >= 700:
    d5 = 0
  if d6 >= 700:
    d6 = 0
  if d7 >= 700:
    d7 = 0

  # Restating the trees
  if t1 >= 700:
    t1 = 0
  if t2 >= 700:
    t2 = 0
  if t3 >= 700:
    t3 = 0
  if t4 >= 700:
    t4 = 0
  if t5 >= 700:
    t5 = 0
  if t6 >= 700:
    t6 = 0
  
  #moving everything else background and your cars with speed
  a1 = a1+speed+car_speed
  c1 = c1+speed+car_speed
  b1 = b1+speed+car_speed
  d1 = d1+speed
  d2 = d2+speed
  d3 = d3+speed
  d4 = d4+speed
  d5 = d5+speed
  d6 = d6+speed
  d7 = d7+speed
  t1 = t1+speed
  t2 = t2+speed
  t3 = t3+speed
  t4 = t4+speed
  t5 = t5+speed
  t6 = t6+speed

  #Creating the Crash logic.
  for k in (x, x+25, x+50):
    for l in (y, y+100):
      #Every point in  Area of my car

      for i in range(a1, a1+100):
        for j in range(a, a+45):
        
          #All 4 corners of front coming cars
          if k == j and l == i:
            crash.play()
            accident(x, y)
            game_over = True

      for i in range(b1, b1+100):
        for j in range(b, b+45):
          if k == j and l == i:
            crash.play()  
            accident(x, y)
            game_over = True

      for i in range(c1, c1+100):
        for j in range(c, c+45):
          if k == j and l == i:
            crash.play()
            accident(x, y)
            game_over = True

  images()

pygame.quit()
