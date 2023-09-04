from turtle import Turtle

STARTING_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = STARTING_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, type):
        if type == 'wall':
            self.y_move *= -1
        elif type == 'paddle':
            self.move_speed *= 0.9
            self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = STARTING_SPEED