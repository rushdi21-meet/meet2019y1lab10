import turtle
import random
import time
import pygame


turtle.penup()
turtle.tracer(1,0)
turtle.goto(-300, 0)
turtle.color("white")

SIZE_X=800
SIZE_Y=500



turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()



pygame.mixer.init()
pygame.mixer.music.load("bell.mp3")


SQUARE_SIZE = 7


turtle.bgpic("seabg.gif")

score_count = 0

SQUARE_SIZE = 5
START_LENGTH = 4
TIME_STAMP = 10
TIME_STEP =  1



time_count = turtle.clone()
time_count.penup()
time_count.goto(0, 0)



Heart=[]
TRASH_LIST = ["bag.gif" , "oil.gif" ,"bottle.gif"]
turtle.direction = "Up"

food_pos = [(400,50) ,(400,-70)]
trash_pos = [(400,100), (300,-100), (200,-50)]
trash= turtle.clone()
trash2= turtle.clone()
trash1= turtle.clone()
food= turtle.clone()
heart= turtle.clone()

turtle.register_shape("heart.gif")
turtle.register_shape("jellyfish.gif") 
turtle.register_shape("oil.gif")
turtle.register_shape("bottle.gif")
turtle.register_shape("bag.gif")
TIME_STEP =  1
trash.shape(random.choice(TRASH_LIST)) 
trash2.shape(random.choice(TRASH_LIST)) 
trash1.shape(random.choice(TRASH_LIST)) 
food.shape("jellyfish.gif")

player_status = "alive"
UP_EDGE = 250
DOWN_EDGE = -250


turtle.register_shape("seaturtle_1.gif")

turtle.register_shape("1.gif")
turtle.register_shape("2.gif")
turtle.register_shape("3.gif")
turtle.shape("seaturtle_1.gif")
trash.hideturtle()
trash1.hideturtle()
trash2.hideturtle()
#heart.hideturtle()
heart.shape("heart.gif")
heart.goto(-350,220)
Heart.append(heart.stamp())
heart.goto(-280, 220)
Heart.append(heart.stamp())
heart.goto(-210,220)
Heart.append(heart.stamp())

time_count.hideturtle()
food.hideturtle()
pygame.mixer.music.play() 
time.sleep(0.5)
time_count.showturtle()
time_count.shape("3.gif")
time.sleep(1)
pygame.mixer.music.play()
time.sleep(0.5)
time_count.shape("2.gif")
time.sleep(1)
pygame.mixer.music.play()
time.sleep(0.5)
time_count.shape("1.gif")
time.sleep(1)
time_count.hideturtle()
trash.showturtle()
trash1.showturtle()
trash2.showturtle()
food.showturtle()

turtle.register_shape("seaturtle_2.gif")
turtle.register_shape("seaturtle_3.gif")
turtle.register_shape("seaturtle_4.gif")
turtle.register_shape("seaturtle_5.gif")
turtle.register_shape("seaturtle_6.gif")
turtle.register_shape("seaturtle_7.gif")
turtle.register_shape("seaturtle_8.gif")
turtle.register_shape("seaturtle_9.gif")
turtle.register_shape("seaturtle_10.gif")
turtle.register_shape("seaturtle_11.gif")
turtle.register_shape("seaturtle_12.gif")
turtle.register_shape("seaturtle_13.gif")
turtle.register_shape("seaturtle_14.gif")
turtle.register_shape("seaturtle_15.gif")
turtle.register_shape("seaturtle_16.gif")
turtle.register_shape("seaturtle_17.gif")
turtle.register_shape("seaturtle_18.gif")
turtle.register_shape("seaturtle_19.gif")
turtle.register_shape("seaturtle_20.gif")
turtle.register_shape("seaturtle_21.gif")
turtle.register_shape("seaturtle_22.gif")
turtle.register_shape("seaturtle_23.gif")
turtle.register_shape("seaturtle_24.gif")
turtle.register_shape("seaturtle_25.gif")
turtle.register_shape("seaturtle_26.gif")
turtle.register_shape("seaturtle_27.gif")
turtle.register_shape("seaturtle_28.gif")


turtle.shape("seaturtle_1.gif")

def up():
    turtle.direction="Up" #Change direction to up
    print("You pressed the up key!")

def down():
    turtle.direction="Down"
    print("You pressed the down key!")

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.listen()

def turtle_animation() :
        while player_status == "alive":
            turtle.shape("seaturtle_1.gif")      
            time.sleep(0.0257)
            turtle.shape("seaturtle_1.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_2.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_3.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_4.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_5.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_6.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_7.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_8.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_9.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_10.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_11.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_12.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_13.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_14.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_15.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_16.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_17.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_18.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_19.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_20.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_21.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_22.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_23.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_24.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_25.gif")
            time.sleep(0.0257)
            
            turtle.shape("seaturtle_26.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_27.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_28.gif")
            

def move_turtle():
    
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if turtle.direction == "Up":
        turtle.goto(x_pos, y_pos + SQUARE_SIZE)
    elif turtle.direction=="Down":
        turtle.goto(x_pos, y_pos - SQUARE_SIZE)



    if y_pos >= UP_EDGE:
        print("You hit the UP EDGE! Game over!")
        quit()
    elif  DOWN_EDGE >= y_pos :
        print("You hit the DOWN EDGE! Game over!")
        quit()

    
   
     
         
    turtle.ontimer(move_turtle,TIME_STAMP)

trash_pos_num = 0

for i in trash_pos:
    trash.penup()
    trash.goto(trash_pos[trash_pos_num])
    trash.pendown()
    trash_pos_num += 1
    trash1.penup()
    trash1.goto(trash_pos[trash_pos_num])
    trash1.pendown()
    trash_pos_num += 1
    trash2.penup()
    trash2.goto(trash_pos[trash_pos_num])
    trash2.pendown()
    trash_pos_num += 1
    if trash_pos_num ==3:
        break

def move_trash():
    global TIME_STEP
    trash.penup()
    trash2.penup()
    trash1.penup()
    trash.backward(SQUARE_SIZE)
    trash1.backward(SQUARE_SIZE)
    trash2.backward(SQUARE_SIZE)
    heart.hideturtle()
    if (trash.xcor()-60 < turtle.xcor()< trash.xcor()+60) and (trash.ycor()-45 <turtle.ycor()< trash.ycor()+45):
        ##turtle.write("you crashed", font = ('Arial', 70))
        #time.sleep(0.3)
        #turtle.clear()
        print("You hit the trash !!")
        clear1 = Heart.pop(-1)
        heart.clearstamp(clear1)
        if len(Heart) ==0:
            turtle.write("GAME OVER", font = ('Arial', 70))
            print("You DIED !!")
            quit()
        trash.backward(130)
    if (trash1.xcor()-60 <turtle.xcor()< trash1.xcor()+60) and (trash1.ycor()-45 <turtle.ycor()< trash1.ycor()+45):
        #turtle.write("you crashed", font = ('Arial', 70))
        #time.sleep(0.3)
        turtle.clear()
        print("You hit the trash!!")
        clear1 = Heart.pop(-1)
        heart.clearstamp(clear1)
        if len(Heart) ==0:
            turtle.write("GAME OVER", font = ('Arial', 70))
            print("You DIED !!")
            quit()
        trash1.backward(130)
    if (trash2.xcor()-60 <turtle.xcor()< trash2.xcor()+60) and (trash2.ycor()-45 <turtle.ycor()< trash2.ycor()+45):
        ##turtle.write("you crashed", font = ('Arial', 70))
        #time.sleep(0.3)
        turtle.clear()
        print("You hit the trash!!")
        clear1 = Heart.pop(-1)
        heart.clearstamp(clear1)
        if len(Heart) ==0:
            turtle.write("GAME OVER", font = ('Arial', 70))
            print("You DIED !!")
            quit()
        trash2.backward(130)
    
    
    #if len(trash_pos) <=4:
    if trash.xcor() <= -410:
        trash.hideturtle()
        make_trash(trash)
    if trash1.xcor() <= -410:
        trash1.hideturtle()
        make_trash(trash1)
    if trash2.xcor() <= -410:
        trash2.hideturtle()
        make_trash(trash2)
        
    turtle.ontimer(move_trash, TIME_STEP)

    
def make_trash(trash_turtle):
    
    min1_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max1_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    
    trash_y = random.randint(min1_y,max1_y)*SQUARE_SIZE
    trash_turtle.penup()
    trash_turtle.shape(random.choice(TRASH_LIST))
    trash_turtle.speed(35)
    trash_turtle.goto(400,trash_y)
    trash_turtle.speed()
    trash_turtle.showturtle()
food_pos_num = 0
for i in food_pos:
    food.penup()
    food.goto(food_pos[food_pos_num])
    food.pendown()
    food_pos_num += 1
    if food_pos_num == 2:
        break

def move_food():
    global TIME_STEP
    food.penup()
    food.backward(SQUARE_SIZE)
    if (food.xcor()-60 < turtle.xcor()< food.xcor()+60) and (food.ycor()-45 <turtle.ycor()< food.ycor()+45):
        print("You ate the jellyfish nice!!!")
        #score_count += 1
        make_food()
    if food.xcor()<= -410:
        food.hideturtle()
        make_food()
    turtle.ontimer(move_food,TIME_STEP)
def make_food():
    min1_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max1_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    food_y = random.randint(min1_y,max1_y)*SQUARE_SIZE
   




    food.penup()
    food.speed(35)
    food.goto(400,food_y)
    food.speed()
    food.showturtle()
    


    

make_food()
move_food()
move_turtle()
move_trash()
turtle_animation()
turtle.mainloop()
