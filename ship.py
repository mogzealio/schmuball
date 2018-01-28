import pygame


class Ship():

    def __init__(self, settings, screen):
        '''Initialise the ship and set its starting position.'''
        # turn parameters into class attributes
        self.screen = screen
        self.settings = settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom centre of the screen.
        # centerx is x-coordinate of the rect centre
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center for finer control
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the ship's position based on the movement flag.'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        # Update rect object (int) from self.center (float)
        self.rect.centerx = self.center  # Only int portion of self.center used

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)
