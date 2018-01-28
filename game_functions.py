import sys
import pygame


def handle_keydown_events(event, ship):
    '''Respond to keydown events.'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def handle_keyup_events(event, ship):
    '''Respond to keyup events.'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    '''Respond to keypresses and mouse events.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Call keydown handling function
            handle_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            # Call keyup handling function
            handle_keyup_events(event, ship)


def update_screen(settings, screen, ship):
    '''Update images on screen and flip to the new screen.'''
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
