import pygame
import colors as c
import algo
from PIL import Image
import sys
from pygame.locals import *
import main_menu

def feedback():
    """feedback menu scherm loop
    Args:
        None
    Returns:
        None
    """
    running = True
    while running:
        #y posities voor de result blokken
        y_pos = 379
        y_pos2 = 379
        y_pos3 = 379
        y_pos4 = 379
        y_pos5 = 379
        y_pos6 = 795
        y_pos7 = 795
        y_pos8 = 795
        y_pos9 = 795
        y_pos10 = 795
        color_code_feedback = []
        color_score_list = []
        mouse = pygame.mouse.get_pos()
        main_menu.screen.fill((240,255,255))
        algo.draw_text('feedback', main_menu.font, c.black, main_menu.screen, 20, 20)

        input = main_menu.clicked_button.values()
        input_tuple = tuple(input)

        #gebruikt algoritme
        algoritme_uitkomst = algo.cosine_sim(input, 10, input_tuple, algo.df_list)
        algoritme_score = algo.cosine_sim_score(input, 10, input_tuple, algo.df_list)

        #klikken komt dan in de lijst
        for color_zero_one in algoritme_uitkomst:
            x = (algo.list_to_color(color_zero_one))
            color_code_feedback.append(x)

        #% berekenen van algoritme score
        for single_score in algoritme_score:
            score_percent = single_score * 100
            score_percent2 = round(score_percent, 2)
            color_score_list.append(score_percent2)


        #elk van de resultaten plaatsen met de info erbij
        score_color_percent = str(color_score_list[0])
        color_names = color_code_feedback[0]
        algo.draw_text(score_color_percent + "%" + " similar",main_menu.font, c.black, main_menu.screen, 20, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 20, y_pos)
            y_pos += 19
        top_1_count = list(algoritme_uitkomst[0])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 20, 335)
        algo.create_image(color_code_feedback[0], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        main_menu.screen.blit(pygame_surface_top1, (20, 40))
        algo.place_liked_buttons(135,350,40,main_menu.screen)
        if 135 + 40 > mouse[0] > 135 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,143,355)

        score_color_percent = str(color_score_list[1])
        color_names = color_code_feedback[1]
        algo.draw_text(score_color_percent + "%" + " similar",main_menu.font, c.black, main_menu.screen, 315, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 315, y_pos2)
            y_pos2 += 19
        top_1_count = list(algoritme_uitkomst[1])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 315, 335)
        algo.create_image(color_code_feedback[1], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        main_menu.screen.blit(pygame_surface_top1, (315, 40))
        algo.place_liked_buttons(430, 350, 40,main_menu.screen)
        if 430 + 40 > mouse[0] > 430 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,438,355)

        score_color_percent = str(color_score_list[2])
        color_names = color_code_feedback[2]
        algo.draw_text(score_color_percent + "%" + " similar", main_menu.font, c.black, main_menu.screen, 610, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 610, y_pos3)
            y_pos3 += 19
        top_1_count = list(algoritme_uitkomst[2])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 610, 335)
        algo.create_image(color_code_feedback[2], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        main_menu.screen.blit(pygame_surface_top1, (610, 40))
        algo.place_liked_buttons(725, 350, 40,main_menu.screen)
        if 725 + 40 > mouse[0] > 725 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,733,355)

        score_color_percent = str(color_score_list[3])
        color_names = color_code_feedback[3]
        algo.draw_text(score_color_percent + "%" + " similar",main_menu.font, c.black, main_menu.screen, 905, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 905, y_pos4)
            y_pos4 += 19
        top_1_count = list(algoritme_uitkomst[3])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 905, 335)
        algo.create_image(color_code_feedback[3], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        main_menu.screen.blit(pygame_surface_top1, (905, 40))
        algo.place_liked_buttons(1010, 350, 40,main_menu.screen)
        if 1010 + 40 > mouse[0] > 1010 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,1018,355)

        score_color_percent = str(color_score_list[4])
        color_names = color_code_feedback[4]
        algo.draw_text(score_color_percent + "%" + " similar",main_menu.font, c.black, main_menu.screen, 1200, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 1200, y_pos5)
            y_pos5 += 19
        top_1_count = list(algoritme_uitkomst[4])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 1200, 335)
        algo.create_image(color_code_feedback[4], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        main_menu.screen.blit(pygame_surface_top1, (1200, 40))
        algo.place_liked_buttons(1315, 350, 40,main_menu.screen)
        if 1315 + 40 > mouse[0] > 1315 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,1323,355)

        score_color_percent = str(color_score_list[5])
        color_names = color_code_feedback[5]
        algo.draw_text(score_color_percent + "%" + " similar",main_menu.font, c.black, main_menu.screen, 20, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 20, y_pos6)
            y_pos6 += 19
        top_1_count = list(algoritme_uitkomst[5])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 20, 751)
        algo.create_image2(color_code_feedback[5], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        main_menu.screen.blit(pygame_surface_top2, (20, 465))
        algo.place_liked_buttons(135, 764, 40,main_menu.screen)
        if 135 + 40 > mouse[0] > 135 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,143,769)

        score_color_percent = str(color_score_list[6])
        color_names = color_code_feedback[6]
        algo.draw_text(score_color_percent + "%" + " similar",main_menu.font, c.black, main_menu.screen, 315, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 315, y_pos7)
            y_pos7 += 19
        top_1_count = list(algoritme_uitkomst[6])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 315, 751)
        algo.create_image2(color_code_feedback[6], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        main_menu.screen.blit(pygame_surface_top2, (315, 465))
        algo.place_liked_buttons(430, 764, 40,main_menu.screen)
        if 430 + 40 > mouse[0] > 430 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,438,769)

        score_color_percent = str(color_score_list[7])
        color_names = color_code_feedback[7]
        algo.draw_text(score_color_percent + "%" + " similar",main_menu.font, c.black, main_menu.screen, 610, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 610, y_pos8)
            y_pos8 += 19
        top_1_count = list(algoritme_uitkomst[7])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 610, 751)
        algo.create_image2(color_code_feedback[7], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        main_menu.screen.blit(pygame_surface_top2, (610, 465))
        algo.place_liked_buttons(725, 764, 40,main_menu.screen)
        if 725 + 40 > mouse[0] > 725 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,733,769)

        score_color_percent = str(color_score_list[8])
        color_names = color_code_feedback[8]
        algo.draw_text(score_color_percent + "%" + " similar",main_menu.font, c.black, main_menu.screen, 905, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 905, y_pos9)
            y_pos9 += 19
        top_1_count = list(algoritme_uitkomst[8])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 905, 751)
        algo.create_image2(color_code_feedback[8], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        main_menu.screen.blit(pygame_surface_top2, (905, 465))
        algo.place_liked_buttons(1010, 764, 40,main_menu.screen)
        if 1010 + 40 > mouse[0] > 1010 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,1018,769)

        score_color_percent = str(color_score_list[9])
        color_names = color_code_feedback[9]
        algo.draw_text(score_color_percent + "%" + " similar",main_menu.font, c.black, main_menu.screen, 1200, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            algo.draw_text("-" + color_name_single, main_menu.font, c.black, main_menu.screen, 1200, y_pos10)
            y_pos10 += 19
        top_1_count = list(algoritme_uitkomst[9])
        most_picks_1 = algo.most_picks(str(top_1_count))
        algo.draw_text(str(most_picks_1) + " votes", main_menu.font, c.black, main_menu.screen, 1200, 751)
        algo.create_image2(color_code_feedback[9], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        main_menu.screen.blit(pygame_surface_top2, (1200, 465))
        algo.place_liked_buttons(1315, 764, 40,main_menu.screen)
        if 1315 + 40 > mouse[0] > 1315 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in main_menu.liked_color_combinations:
                main_menu.liked_color_combinations.append(color_names)
                algo.draw_text("X",pygame.font.SysFont(None, 55),c.black, main_menu.screen,1323,769)
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
        main_menu.mainClock.tick(20)

