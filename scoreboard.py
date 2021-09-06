ALIGNMENT='center'
FONT=('Ariel',20,'normal')

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        with open("data.txt") as data:
           self.high_score = int(data.read())
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score}             High score:{self.high_score}",align=ALIGNMENT,font=FONT)
    
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()     
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                self.high_score = data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
            
        
    
        