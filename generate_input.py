import pygame
import colors as c
import algo
import sys
from pygame.locals import *
import main_menu

def generate():
    """generate menu scherm loop
    Args:
        None
    Returns:
        None
    """
    running = True
    while running:
        y_pos = 185
        main_menu.screen.fill((240,255,255))
        algo.draw_text('generated', pygame.font.SysFont(None, 45), c.black, main_menu.screen, 835, 50)
        algo.create_image(main_menu.clicked_button_list_codes, 640)
        randomly_generated_image1 = pygame.image.load('image.png')
        main_menu.screen.blit(randomly_generated_image1, (600, 100))


        input_list_user = (list(main_menu.clicked_button.values()))
        top_count = algo.most_picks(str(input_list_user))
        algo.draw_text(str(top_count) + " votes", pygame.font.SysFont(None, 50), c.black, main_menu.screen, 75, 100)

        for single_color in main_menu.clicked_button_list:
            algo.draw_text("-" + single_color, pygame.font.SysFont(None, 50), c.black, main_menu.screen, 75, y_pos)
            y_pos += 45

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        main_menu.mainClock.tick(25)