import pygame
from color import *
from calculation import *

class Button:
    def __init__(self, super_surface_object, text, color, x, y, front_size=28):
        self.font = pygame.font.Font('../resources/font/OpenSans-Semibold.ttf', front_size)
        self.text = text
        self.hover = False
        self.color = color

        self.surface = self.font.render(self.text, True, self.color)

        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        self.super_surface = super_surface_object.surface
        self.super_surface_object = super_surface_object

        position = blit_position_transfer(self.super_surface, self.surface, x, y)

        self.x = position[0]
        self.y = position[1]
        self.display()

    def display(self):
        self.super_surface.blit(self.surface, (self.x, self.y))
        self.super_surface_object.update()

    def update(self):
        self.display()

    def remove(self):
        self.surface.fill(LIGHTBLUE)
        self.update()

    def check_click(self, position):
        x_match = position[0] > self.x and position[0] < self.x + self.width
        y_match = position[1] > self.y and position[1] < self.y + self.height
        global cursor_state
        if x_match and y_match:
            if self.hover != True:
                self.hover = True
                cursor_state = "hand"
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            if self.hover != False:
                self.hover = False
                cursor_state = "normal"
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return self.hover

    def change(self, color=None, text = None):
        if color:
            self.color = color
        if text:
            self.text = text
        self.surface = self.font.render(self.text, True, self.color)
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.display()
