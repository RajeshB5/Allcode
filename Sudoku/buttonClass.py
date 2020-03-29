import pygame

class Button:
    def __init__(self, x, y, height, width, text=None, colour=(73, 73, 73), highLightedColour=(189, 189, 189), function=None, params=None):
        self.image = pygame.Surface((width, height))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.function = function
        self.params = params
        self.highLightedColour = highLightedColour
        self.colour = colour
        self.highLighted = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highLighted = True
        else:
            self.highLighted = False

    def draw(self, window):
        if self.highLighted:
            self.image.fill(self.highLightedColour)
        else:
            self.image.fill(self.colour)
        window.blit(self.image, self.pos)