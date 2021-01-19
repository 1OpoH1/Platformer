import pygame

from classes.Collider import Collider
from classes.EntityCollider import EntityCollider
from classes.Maths import Vec2D
from entities.EntityBase import EntityBase


class Finish(EntityBase):
    def __init__(self, screen, spriteColl, x, y, level):
        super(Finish, self).__init__(y, x - 1, 1.25)
        self.spriteCollection = spriteColl
        self.image = self.spriteCollection.get("finish").image
        self.rect = pygame.Rect(x * 32, y * 32, 32, 32)
        self.screen = screen
        self.type = "Mob"
        self.dashboard = level.dashboard
        self.collision = Collider(self, level)
        self.EntityCollider = EntityCollider(self)
        self.levelObj = level
        self.textPos = Vec2D(0, 0)
        self.alive = True

    def update(self, camera):
        if self.alive:
            self.applyGravity()
            self.drawFinish(camera)
        else:
            pass

    def drawFinish(self, camera):
        self.screen.blit(self.image, (self.rect.x + camera.x, self.rect.y))

    def setPointsTextStartPosition(self, x, y):
        self.textPos = Vec2D(x, y)

    def movePointsTextUpAndDraw(self, camera):
        self.textPos.y += -0.5
        self.dashboard.drawText("100", self.textPos.x + camera.x, self.textPos.y, 8)