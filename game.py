import turtle
import time
import random

#Declare the scores and delay
delay = 0.3
score = 0

#Creating the game setting
game = turtle.Screen()
game.title("THEEE Snake Game")
game.bgcolor("aqua")
game.setup(width = 100, height = 100)
game.tracer(0)

#The snakes head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food for the snake
food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.speed(0)
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0 High Score : 0", align = "center", font = ("Comic Sans MS", 24, "bold"))
turtle.done()

