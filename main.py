from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 

# Setup the screen
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#creating objects
snake=Snake()
food=Food()
scoreboard=Scoreboard()

#getting directions from the keyboard inputs
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    #determains how fast the snake moves. 
    time.sleep(0.1)
    snake.move()
    
    
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
        
   
    #detect collision with wall
    
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()
        
    # Detect collision with tail
    for segment in snake.snake[ 1: ]:
        
        if snake.head.distance(segment) < 5:
            scoreboard.game_reset()
            snake.reset()
        
        
screen.exitonclick()






