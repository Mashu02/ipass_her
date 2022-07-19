import sys
import pygame
import colors as c
import buttons as b
import algo
from pygame.locals import *
import random_generate

mainClock = pygame.time.Clock()
pygame.init()

#screen
screen = pygame.display.set_mode((1536, 870))
pygame.display.set_caption('color matcher')
font = pygame.font.SysFont(None, 20)
click = False
mouse = pygame.mouse.get_pos()
clicked_button = {"Black" : 0,  "Grey" : 0,  "Silver" : 0,  "White" : 0,  "Brown" : 0,
                  "Red" : 0,  "Orange" : 0,  "Gold" : 0,  "Beige" : 0,  "Yellow" : 0,
                  "Green" : 0,  "Turqoise" : 0,  "Teal" : 0,  "Blue" : 0,  "Violet" : 0,
                  "Purple" : 0,  "Pink" : 0}
clicked_button_list = []
clicked_button_list_codes = []
liked_color_combinations = []
color_name_liked_combo = []


def main_menu_loop():
    """main menu scherm loop
    Args:
        None
    Returns:
        None
    """
    while True:
        #scherm kleur
        screen.fill((240,255,255))
        algo.draw_text('Pick color(s)', pygame.font.SysFont(None, 50), c.black, screen, 275, 35)
        algo.draw_text('Selected colors', pygame.font.SysFont(None, 50), c.black, screen, 695, 35)
        algo.draw_text('Your liked combinations:', pygame.font.SysFont(None, 50), c.black, screen, 1065, 35)
        y_pos = 92
        y_pos_color_code = 92
        input_rgb = algo.list_to_color(clicked_button.values())
        input_hsv = algo.list_to_color_hsv(clicked_button.values())
        #muis positie
        mouse = pygame.mouse.get_pos()

        #button maken
        button_generate = pygame.Rect(696, 700, 301, 100)
        button_generate_outline = pygame.Rect(693, 697, 307, 106)

        button_feedback = pygame.Rect(230, 700, 401, 100)
        button_feedback_outline = pygame.Rect(227,697,407,106)

        button_clear = pygame.Rect(1065, 700, 280, 100)
        button_clear_outline = pygame.Rect(1062, 697, 286, 106)

        button_save = pygame.Rect(1380, 700, 130, 100)
        button_save_outline = pygame.Rect(1377, 697, 136, 106)


        #is voor de buttons wanneer de muis tussen de x en y waardes zit

        if b.button_black.collidepoint((mouse)):
            if click:
                if clicked_button["Black"] == 1 or (0, 0, 0) in clicked_button_list_codes or "Black" in clicked_button_list:
                    clicked_button["Black"] = 0
                    clicked_button_list_codes.remove((0, 0, 0))
                    clicked_button_list.remove("Black")
                else:
                    clicked_button["Black"] = 1
                    clicked_button_list_codes.append((0, 0, 0))
                    clicked_button_list.append("Black")
        elif b.button_grey.collidepoint((mouse)):
            if click:
                if clicked_button["Grey"] == 1 or (128,128,128) in clicked_button_list_codes or "Grey" in clicked_button_list:
                    clicked_button["Grey"] = 0
                    clicked_button_list_codes.remove((128,128,128))
                    clicked_button_list.remove("Grey")
                else:
                    clicked_button["Grey"] = 1
                    clicked_button_list_codes.append((128,128,128))
                    clicked_button_list.append("Grey")
        elif b.button_silver.collidepoint((mouse)):
            if click:
                if clicked_button["Silver"] == 1 or (192,192,192) in clicked_button_list_codes or "Silver" in clicked_button_list:
                    clicked_button["Silver"] = 0
                    clicked_button_list_codes.remove((192,192,192))
                    clicked_button_list.remove("Silver")
                else:
                    clicked_button["Silver"] = 1
                    clicked_button_list_codes.append((192,192,192))
                    clicked_button_list.append("Silver")
        elif b.button_white.collidepoint((mouse)):
            if click:
                if clicked_button["White"] == 1 or (255,255,255) in clicked_button_list_codes or "White" in clicked_button_list:
                    clicked_button["White"] = 0
                    clicked_button_list_codes.remove((255,255,255))
                    clicked_button_list.remove("White")
                else:
                    clicked_button["White"] = 1
                    clicked_button_list_codes.append((255,255,255))
                    clicked_button_list.append("White")
        elif b.button_brown.collidepoint((mouse)):
            if click:
                if clicked_button["Brown"] == 1 or (139,69,19) in clicked_button_list_codes or "Brown" in clicked_button_list:
                    clicked_button["Brown"] = 0
                    clicked_button_list_codes.remove((139,69,19))
                    clicked_button_list.remove("Brown")
                else:
                    clicked_button["Brown"] = 1
                    clicked_button_list_codes.append((139,69,19))
                    clicked_button_list.append("Brown")
        elif b.button_red.collidepoint((mouse)):
            if click:
                if clicked_button["Red"] == 1 or (255,0,0) in clicked_button_list_codes or "Red" in clicked_button_list:
                    clicked_button["Red"] = 0
                    clicked_button_list_codes.remove((255,0,0))
                    clicked_button_list.remove("Red")
                else:
                    clicked_button["Red"] = 1
                    clicked_button_list_codes.append((255,0,0))
                    clicked_button_list.append("Red")
        elif b.button_orange.collidepoint((mouse)):
            if click:
                if clicked_button["Orange"] == 1 or (255,150,0) in clicked_button_list_codes or "Orange" in clicked_button_list:
                    clicked_button["Orange"] = 0
                    clicked_button_list_codes.remove((255,150,0))
                    clicked_button_list.remove("Orange")
                else:
                    clicked_button["Orange"] = 1
                    clicked_button_list_codes.append((255,150,0))
                    clicked_button_list.append("Orange")
        elif b.button_gold.collidepoint((mouse)):
            if click:
                if clicked_button["Gold"] == 1 or (255,215,0) in clicked_button_list_codes or "Gold" in clicked_button_list:
                    clicked_button["Gold"] = 0
                    clicked_button_list_codes.remove((255,215,0))
                    clicked_button_list.remove("Gold")
                else:
                    clicked_button["Gold"] = 1
                    clicked_button_list_codes.append((255,215,0))
                    clicked_button_list.append("Gold")
        elif b.button_beige.collidepoint((mouse)):
            if click:
                if clicked_button["Beige"] == 1 or (245,245,220) in clicked_button_list_codes or "Beige" in clicked_button_list:
                    clicked_button["Beige"] = 0
                    clicked_button_list_codes.remove((245,245,220))
                    clicked_button_list.remove("Beige")
                else:
                    clicked_button["Beige"] = 1
                    clicked_button_list_codes.append((245,245,220))
                    clicked_button_list.append("Beige")
        elif b.button_yellow.collidepoint((mouse)):
            if click:
                if clicked_button["Yellow"] == 1 or (255,255,0) in clicked_button_list_codes or "Yellow" in clicked_button_list:
                    clicked_button["Yellow"] = 0
                    clicked_button_list_codes.remove((255,255,0))
                    clicked_button_list.remove("Yellow")
                else:
                    clicked_button["Yellow"] = 1
                    clicked_button_list_codes.append((255,255,0))
                    clicked_button_list.append("Yellow")
        elif b.button_green.collidepoint((mouse)):
            if click:
                if clicked_button["Green"] == 1 or (0,128,0) in clicked_button_list_codes or "Green" in clicked_button_list:
                    clicked_button["Green"] = 0
                    clicked_button_list_codes.remove((0,128,0))
                    clicked_button_list.remove("Green")
                else:
                    clicked_button["Green"] = 1
                    clicked_button_list_codes.append((0,128,0))
                    clicked_button_list.append("Green")
        elif b.button_turqoise.collidepoint((mouse)):
            if click:
                if clicked_button["Turqoise"] == 1 or (64,224,208) in clicked_button_list_codes or "Turqoise" in clicked_button_list:
                    clicked_button["Turqoise"] = 0
                    clicked_button_list_codes.remove((64,224,208))
                    clicked_button_list.remove("Turqoise")
                else:
                    clicked_button["Turqoise"] = 1
                    clicked_button_list_codes.append((64,224,208))
                    clicked_button_list.append("Turqoise")
        elif b.button_teal.collidepoint((mouse)):
            if click:
                if clicked_button["Teal"] == 1 or (0,128,128) in clicked_button_list_codes or "Teal" in clicked_button_list:
                    clicked_button["Teal"] = 0
                    clicked_button_list_codes.remove((0,128,128))
                    clicked_button_list.remove("Teal")
                else:
                    clicked_button["Teal"] = 1
                    clicked_button_list_codes.append((0,128,128))
                    clicked_button_list.append("Teal")
        elif b.button_blue.collidepoint((mouse)):
            if click:
                if clicked_button["Blue"] == 1 or (0,0,255) in clicked_button_list_codes or "Blue" in clicked_button_list:
                    clicked_button["Blue"] = 0
                    clicked_button_list_codes.remove((0,0,255))
                    clicked_button_list.remove("Blue")
                else:
                    clicked_button["Blue"] = 1
                    clicked_button_list_codes.append((0,0,255))
                    clicked_button_list.append("Blue")
        elif b.button_violet.collidepoint((mouse)):
            if click:
                if clicked_button["Violet"] == 1 or (238,130,238) in clicked_button_list_codes or "Violet" in clicked_button_list:
                    clicked_button["Violet"] = 0
                    clicked_button_list_codes.remove((238,130,238))
                    clicked_button_list.remove("Violet")
                else:
                    clicked_button["Violet"] = 1
                    clicked_button_list_codes.append((238,130,238))
                    clicked_button_list.append("Violet")
        elif b.button_purple.collidepoint((mouse)):
            if click:
                if clicked_button["Purple"] == 1 or (128,0,128) in clicked_button_list_codes or "Purple" in clicked_button_list:
                    clicked_button["Purple"] = 0
                    clicked_button_list_codes.remove((128,0,128))
                    clicked_button_list.remove("Purple")
                else:
                    clicked_button["Purple"] = 1
                    clicked_button_list_codes.append((128,0,128))
                    clicked_button_list.append("Purple")
        elif b.button_pink.collidepoint((mouse)):
            if click:
                if clicked_button["Pink"] == 1 or (255,105,180) in clicked_button_list_codes or "Pink" in clicked_button_list:
                    clicked_button["Pink"] = 0
                    clicked_button_list_codes.remove((255,105,180))
                    clicked_button_list.remove("Pink")
                else:
                    clicked_button["Pink"] = 1
                    clicked_button_list_codes.append((255,105,180))
                    clicked_button_list.append("Pink")

        elif button_generate.collidepoint((mouse)):
            if click and len(clicked_button_list) != 0:
                random_generate.random_horizontal(input_rgb)
                random_generate.random_vertical(input_rgb)
                random_generate.random_circle(input_rgb)
                random_generate.random_rect(input_rgb)
                random_generate.random_diagonal(input_rgb)
                generate()
        elif button_feedback.collidepoint((mouse)):
            if click and len(clicked_button_list) != 0:
                random_generate.random_horizontal(input_rgb)
                random_generate.random_vertical(input_rgb)
                random_generate.random_circle(input_rgb)
                random_generate.random_rect(input_rgb)
                random_generate.random_diagonal(input_rgb)
                feedback()
        elif button_clear.collidepoint((mouse)):
            if click:
                liked_color_combinations.clear()
        elif button_save.collidepoint((mouse)):
            if click:
                algo.list_to_clipboard(str(liked_color_combinations))
                algo.draw_text('copied to clipboard!', pygame.font.SysFont(None, 35), c.black, screen, 1250, 630)


        #button placen
        pygame.draw.rect(screen, c.black, button_feedback_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_feedback)

        pygame.draw.rect(screen, c.black, button_generate_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_generate)

        pygame.draw.rect(screen, c.black, button_clear_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_clear)

        pygame.draw.rect(screen, c.black, button_save_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_save)

        #text plaatsen
        algo.draw_text('show result', pygame.font.SysFont(None, 60), c.black, screen, 310, 730)
        algo.draw_text('generate input', pygame.font.SysFont(None, 40), c.black, screen, 746, 735)
        algo.draw_text('clear combinations', pygame.font.SysFont(None, 40), c.black, screen, 1070, 735)
        algo.draw_text('copy', pygame.font.SysFont(None, 40), c.black, screen, 1410, 735)
        click = False

        #kleur buttons plaatsen
        algo.place_button(c.black, b.out_button_black, screen)
        algo.place_button(c.black, b.button_black, screen)
        algo.place_button(c.black, b.out_button_grey, screen)
        algo.place_button(c.grey, b.button_grey, screen)
        algo.place_button(c.black, b.out_button_silver, screen)
        algo.place_button(c.silver, b.button_silver, screen)
        algo.place_button(c.black, b.out_button_white, screen)
        algo.place_button(c.white, b.button_white, screen)
        algo.place_button(c.black, b.out_button_brown, screen)
        algo.place_button(c.brown, b.button_brown, screen)
        algo.place_button(c.black, b.out_button_red, screen)
        algo.place_button(c.red, b.button_red, screen)
        algo.place_button(c.black, b.out_button_orange, screen)
        algo.place_button(c.orange, b.button_orange, screen)
        algo.place_button(c.black, b.out_button_gold, screen)
        algo.place_button(c.gold, b.button_gold, screen)
        algo.place_button(c.black, b.out_button_beige, screen)
        algo.place_button(c.beige, b.button_beige, screen)
        algo.place_button(c.black, b.out_button_yellow, screen)
        algo.place_button(c.yellow, b.button_yellow, screen)
        algo.place_button(c.black, b.out_button_green, screen)
        algo.place_button(c.green, b.button_green, screen)
        algo.place_button(c.black, b.out_button_turqoise, screen)
        algo.place_button(c.turqoise, b.button_turqoise, screen)
        algo.place_button(c.black, b.out_button_teal, screen)
        algo.place_button(c.teal, b.button_teal, screen)
        algo.place_button(c.black, b.out_button_blue, screen)
        algo.place_button(c.blue, b.button_blue, screen)
        algo.place_button(c.black, b.out_button_violet, screen)
        algo.place_button(c.violet, b.button_violet, screen)
        algo.place_button(c.black, b.out_button_purple, screen)
        algo.place_button(c.purple, b.button_purple, screen)
        algo.place_button(c.black, b.out_button_pink, screen)
        algo.place_button(c.pink, b.button_pink, screen)

        #color list in selected
        for single_color in clicked_button_list:
            algo.draw_text("-"+single_color, pygame.font.SysFont(None, 25), c.black, screen, 685, y_pos)
            y_pos += 20

        for liked_color_combo in liked_color_combinations:
            algo.draw_text(str(liked_color_combo), pygame.font.SysFont(None, 25), c.black, screen, 1100, y_pos_color_code)
            y_pos_color_code += 25

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(25)

def generate():
    """generate menu scherm loop
    Args:
        None
    Returns:
        None
    """
    running = True
    while running:

        y_pos = 60
        mouse = pygame.mouse.get_pos()
        screen.fill((240,255,255))
        algo.draw_text('generated', pygame.font.SysFont(None, 30), c.black, screen, 835, 5)
        algo.create_image(clicked_button_list_codes, 640)

        input_list_user = (list(clicked_button.values()))
        input_rgb = algo.list_to_color(clicked_button.values())
        top_count = algo.most_picks(str(input_list_user))
        algo.draw_text(str(top_count) + " votes", pygame.font.SysFont(None, 30), c.black, screen, 75, 25)

        for single_color in clicked_button_list:
            algo.draw_text("-" + single_color, pygame.font.SysFont(None, 35), c.black, screen, 75, y_pos)
            y_pos += 25

        button_generate = pygame.Rect(50, y_pos + 25, 150, 100)
        button_generate_outline = pygame.Rect(47, y_pos + 22, 157, 106)

        pygame.draw.rect(screen, c.black, button_generate_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_generate)

        #plaats de pngs, kijk dc voor hoe eruit zien
        horizontal = pygame.image.load('horizontal.png')
        horizontal1 = pygame.transform.scale(horizontal, (300,300))
        screen.blit(horizontal1, (250,50))

        vertical = pygame.image.load('vertical.png')
        vertical1 = pygame.transform.scale(vertical, (300, 300))
        screen.blit(vertical1, (735, 50))

        diagonal = pygame.image.load('diagonal.png')
        diagonal1 = pygame.transform.scale(diagonal, (300, 300))
        screen.blit(diagonal1, (1220, 50))

        diagonal2 = pygame.image.load('diagonal2.png')
        diagonal12 = pygame.transform.scale(diagonal2, (300, 300))
        screen.blit(diagonal12, (250, 535))

        circle = pygame.image.load('circle.png')
        circle1 = pygame.transform.scale(circle,(300, 300))
        screen.blit(circle1, (735, 535))

        rect = pygame.image.load('rect.png')
        rect1 = pygame.transform.scale(rect, (300, 300))
        screen.blit(rect1, (1220, 535))

        if button_generate.collidepoint(mouse):
            if click:
                random_generate.random_horizontal(input_rgb)
                random_generate.random_vertical(input_rgb)
                random_generate.random_circle(input_rgb)
                random_generate.random_rect(input_rgb)
                random_generate.random_diagonal(input_rgb)


        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def feedback():
    """feedback menu scherm loop
    Args:
        None
    Returns:
        None
    """
    running = True
    while running:
        y_pos = 60
        rgb_list_input = []
        mouse = pygame.mouse.get_pos()
        screen.fill((240,255,255))
        algo.draw_text('feedback', font, c.black, screen, 20, 20)

        button_generate = pygame.Rect(50, y_pos + 25, 150, 100)
        button_generate_outline = pygame.Rect(47, y_pos + 22, 157, 106)

        pygame.draw.rect(screen, c.black, button_generate_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_generate)

        input_hsv = algo.list_to_color_hsv(clicked_button.values())
        input_rgb = algo.list_to_color(clicked_button.values())
        #van klein naar groot sorteren voor berekenen v1,v2 en v1,v3
        sorted(input_hsv, key=lambda x: x[0])

        input_angle = (algo.calc_angle(input_hsv))
        z = algo.get_higest_sim_in_hsv(input_angle)
        print(z)

        #de hsv naar rgb en dan generaten met de recommendation



        #rgb voor images
        #hsv voor berekenen
        # if len(input) == 1:
        #
        # else:
        #
        # angle = algo.calc_angle(input)
        # print(angle)

        # plaats de pngs, kijk dc voor hoe eruit zien
        horizontal = pygame.image.load('horizontal.png')
        horizontal1 = pygame.transform.scale(horizontal, (300, 300))
        screen.blit(horizontal1, (250, 50))

        vertical = pygame.image.load('vertical.png')
        vertical1 = pygame.transform.scale(vertical, (300, 300))
        screen.blit(vertical1, (735, 50))

        diagonal = pygame.image.load('diagonal.png')
        diagonal1 = pygame.transform.scale(diagonal, (300, 300))
        screen.blit(diagonal1, (1220, 50))

        diagonal2 = pygame.image.load('diagonal2.png')
        diagonal12 = pygame.transform.scale(diagonal2, (300, 300))
        screen.blit(diagonal12, (250, 535))

        circle = pygame.image.load('circle.png')
        circle1 = pygame.transform.scale(circle, (300, 300))
        screen.blit(circle1, (735, 535))

        rect = pygame.image.load('rect.png')
        rect1 = pygame.transform.scale(rect, (300, 300))
        screen.blit(rect1, (1220, 535))

        if button_generate.collidepoint(mouse):
            if click:
                random_generate.random_horizontal(input_rgb)
                random_generate.random_vertical(input_rgb)
                random_generate.random_circle(input_rgb)
                random_generate.random_rect(input_rgb)
                random_generate.random_diagonal(input_rgb)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

#voor pydoc generate
if __name__ == '__main__':
    main_menu_loop()