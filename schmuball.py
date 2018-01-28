import pygame
from settings import Settings
from ship import Ship
import game_functions as gf  # alias


def run_game():
    # Initialise game and create a screen object.'''
    pygame.init()

    # Create an instance of Settings class
    sb_settings = Settings()

    # Create main display surface
    screen = pygame.display.set_mode(
        (sb_settings.screen_width, sb_settings.screen_height))
    pygame.display.set_caption("Schmuball")

    # Make an instance of Ship class, passing settings and screen as arguments
    ship = Ship(sb_settings, screen)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events, passing ship as argument
        gf.check_events(ship)
        # Call update function in ship instance
        ship.update()
        # Redraw the screen
        gf.update_screen(sb_settings, screen, ship)


run_game()
