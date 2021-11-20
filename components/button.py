import pygame
from color import *
from calculation import *

class Button:
    def __init__(self, super_surface_object, text, color, x, y):
        self.font = pygame.font.Font('../resources/font/OpenSans-Semibold.ttf', 28)
        self.text = text

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

    # def update_together(self):
    #     self.super_surface.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        x_match = position[0] > self.x and position[0] < self.x + self.width
        y_match = position[1] > self.y and position[1] < self.y + self.height
        global cursor_state
        if x_match and y_match:
            if cursor_state != "hand":
                cursor_state = "hand"
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            return True
        else:
            if cursor_state != "normal":
                cursor_state = "normal"
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return False

    def change(self, color=None, text = None):
        if color:
            self.color = color
        if text:
            self.text = text
        self.surface = self.font.render(self.text, True, self.color)
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.display()

    # # Display settlement circle button
    # def display_settlement_button(self, hover):
    #     if hover:
    #         # pygame.draw.circle(self.surface, self.hover_color, ((self.x), (self.y)), 10)
    #         pygame.draw.circle(self.surface, self.hover_color, (self.width/2, self.height/2), 10)
    #     else:
    #         # pygame.draw.circle(self.surface, self.color, ((self.x),(self.y)), 10)
    #         pygame.draw.circle(self.surface, self.color, (self.width/2, self.height/2), 10)
    #     self.update_together()
    #
    #
    # def get_pos(self):
    #     return (self.x, self.y)
    #
    # def change_button_color(self, color, hover_color):
    #     self.color = color
    #     self.hover_color = hover_color
