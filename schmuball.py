import pygame
from settings import Settings
from ship import Ship
import game_functions as gf  # alias


def run_game():
    # Initialise game and create a screen object.'''
    pygame.init()
    # Create an instance of Settings class
    sb_settings = Settings()
    # The use attributes of the newly created instance of Settings
    screen = pygame.display.set_mode(
        (sb_settings.screen_width, sb_settings.screen_height))
    pygame.display.set_caption("Schmuball")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events()
        gf.update_screen(sb_settings, screen, ship)


run_game()
