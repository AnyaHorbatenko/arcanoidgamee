import random

import pgzrun
import pygame as pg


WIDTH = 800
HEIGHT = 600

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect((self.x, self. y), (self.width, self.height))

    def draw(self):
        screen.draw.filled_rect(Rect((self.x, self.y), (self.width, self.height)), (255, 255, 255))

    def update(self):
        self.x = pg.mouse.get_pos()[0]
        if self.x < -100:
            self.x = 0
        if self.x > WIDTH-50:
            self.x = WIDTH-100

    def check_collision(self, ball):
        if ball.x + ball.radius > self.x and ball.x < self.x + self.width and ball.y + ball.radius > self.y and ball.y < self.y + self.height:
        #if ball.x > self.x and ball.x < self.x + self.width and ball.y > self.y and ball.y < self.y + self.height:
            ball.VelocityY = -ball.VelocityY
    def check_collision_bonuses(self, bonus):
        global lives
        if bonus.x > self.x and bonus.x < self.x + self.width and bonus.y > self.y and bonus.y < self.y + self.height:
            bonuses.remove(bonus)
            lives += 1

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.VelocityX = 5
        self.VelocityY = 5

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, "Yellow")

    def update(self):
        self.x += self.VelocityX
        self.y += self.VelocityY

        if self.x > WIDTH or self.x < 0:
            self.VelocityX = -self.VelocityX
        if self.y > HEIGHT or self.y < 0:
            self.VelocityY = -self.VelocityY

class Brick:
    def __init__(self, x, y, width, height, lives, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = True
        self.lives = lives
        self.colour = colour

    def draw(self):
        if self.active:
            screen.draw.filled_rect(Rect((self.x, self.y), (self.width, self.height)), self.colour)

    def check_collision(self, ball):
        if self.active and ball.x + ball.radius > self.x and ball.x < self.x + self.width and ball.y + ball.radius > self.y and ball.y < self.y + self.height:
        #if self.active and ball.x > self.x and ball.x < self.x + self.width and ball.y > self.y and ball.y < self.y + self.height:
            ball.VelocityY = -ball.VelocityY
            self.lives -= 1
            if self.lives == 0:
                self.active = False
                return True
        return False

class Bonus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.velocity = 100

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), 5, "Purple")

    def move(self,dt):
         self.y += self.velocity * dt

