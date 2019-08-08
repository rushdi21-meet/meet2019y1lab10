import turtle
import random

SQUARE_SIZE = 7
turtle.bgpic("seabg.gif")

SIZE_X=800
SIZE_Y=520

turtle.setup(SIZE_X,SIZE_Y)
turtle.register_shape("oil.gif")
turtle.register_shape("bottle.gif")
turtle.register_shape("bag.gif")
TRASH_LIST = ["bag.gif" , "oil.gif" ,"bottle.gif"]

##turtle.penup()
trash= turtle.clone()
trash2= turtle.clone()
trash1= turtle.clone()

turtle.hideturtle()
TIME_STEP =  1
trash.shape(random.choice(TRASH_LIST)) 
trash2.shape(random.choice(TRASH_LIST)) 
trash1.shape(random.choice(TRASH_LIST)) 


#trash.tracer(1,0)
#trash1.tracer(1,0)
#trash2.tracer(1,0)
#Locations of poison
trash_pos = [(400,100), (400,-100), (200,-50)]
#while True:
 #   trash.penup()
 #   trash1.penup()
 #   trash2.penup()
 
# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!
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
    if turtle.pos() in trash_pos:
        trash_index=trash_pos.index(turtle.pos()) #What does this do?
        trash_pos.pop(trash_index) #Remove eaten food position
        print("You have eaten the the poison lol!!")
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
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min1_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max1_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    trash_y = random.randint(min1_y,max1_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    trash_turtle.penup()
    trash_turtle.shape(random.choice(TRASH_LIST))
    trash_turtle.speed(35)
    trash_turtle.goto(400,trash_y)
    trash_turtle.speed()
    trash_turtle.showturtle()
    
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list

move_trash()
turtle.mainloop()
