import pygame
import sys
import options
import os
import json
import random
from time import sleep
 
f = open('Options/bg.json')
bgcs = json.load(f)

ld=1

#init
pygame.init()
pygame.font.init()

#fps
fps = pygame.time.Clock()
fps.tick(60)

#setup screen
dx = 1080 #dai
dy = 680 # rong
display = pygame.display.set_mode((dx, dy)) #tao man hinh
pygame.display.set_caption("Pong Game") # dat tieu de
bg01 = pygame.image.load('bg.jpg')
bg02 = pygame.image.load('Asset/background/bg-01.png')
bg03 = pygame.image.load('Asset/background/bg-02.jpg')
bg_se = bg01
bg_va = 1
bg_se = pygame.transform.scale(bg_se,(dx,dy))


if bgcs == 1:
    bg_se = bg01
    bg_se = pygame.transform.scale(bg_se,(dx,dy))
if bgcs == 2:
    bg_se = bg02
    bg_se = pygame.transform.scale(bg_se,(dx,dy))
if bgcs == 3:
    bg_se = bg03
    bg_se = pygame.transform.scale(bg_se,(dx,dy))
#mau
df_bg_color = 0,0,0 #mau mac dinh 

#chu




def f_arial(size):
    return pygame.font.SysFont("Arial", size)


#chay 


def main():
    main_button_blue = 0, 102, 204
    main_button_blue2 = 0, 102, 204
    Title_text = f_arial(50).render("Pong Game", True, (255,255,255))

    play_text = f_arial(50).render("Play", True, (255,255,255))

    options_text = f_arial(50).render("Options", True, (255,255,255))
    version_text = f_arial(20).render("Version: 1 beta 1 by Minhtriet349", True, (255,255,255))
    while True:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 440 <= pos[0] <= 640 and 200 <= pos[1] <= 300:
                    main_button_blue = 0, 204, 255
                if 440 <= pos[0] <= 640 and 400 <= pos[1] <= 500:
                    main_button_blue2 = 0, 204, 255


                print(pos)

            if event.type == pygame.MOUSEBUTTONUP:
                main_button_blue = 0, 102, 204
                main_button_blue2 = 0, 102, 204
                if 440 <= pos[0] <= 640 and 200 <= pos[1] <= 300:
                    play()
                if 440 <= pos[0] <= 640 and 400 <= pos[1] <= 500:
                    option()



        display.fill((df_bg_color))
        display.blit(bg_se, (0,50))
        pygame.draw.rect(display,(0, 102, 204) ,(0,0,dx,50))
        display.blit(Title_text, (430,0))
        pygame.draw.rect(display,(main_button_blue), (440,200,200,100))
        display.blit(play_text, (500,220))
        pygame.draw.rect(display,(main_button_blue2), (440,400,200,100))
        display.blit(options_text, (470,420))
        display.blit(version_text, (2,655))
        pygame.display.update()




    pygame.quit()

def play():
    player_1_y = 265
    player_2_y = 265
    player_2_x = 1045
    player_1_x = 5
    ball_x = 60
    ball_y = 340
    ball_x_change = 1
    ball_y_change = 1
    b = random.randint(0,1)
    #0,1 khoi dau va ben trai
    #2,3 va cham tren
    #4,5 va cham duoi
    #6,7 ben phai
    play_1_y_change = 0
    play_2_y_change = 0
    po = 'Right'
    while True:
        pos_pl = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    play_1_y_change = 1
                if event.key == pygame.K_w:
                    play_1_y_change = -1
                if event.key == pygame.K_UP:
                    play_2_y_change = -1
                if event.key == pygame.K_DOWN:
                    play_2_y_change = 1
                if event.key == pygame.K_SPACE:
                    main()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or pygame.K_w:
                    play_1_y_change = 0
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    play_2_y_change = 0



        player_1_y += play_1_y_change
        player_2_y += play_2_y_change
        display.fill((155,155,155))
        display.blit(bg_se, (0,0))
        pygame.draw.rect(display, (255,255,255), (10,10,50,50))
        pygame.draw.rect(display, (155, 155, 155), (0,0,dx, 60))
        pygame.draw.rect(display, (0, 102, 204), (player_1_x , player_1_y, 30, 150))
        pygame.draw.rect(display, (0, 102, 204), (player_2_x, player_2_y, 30, 150))
        pygame.draw.circle(display, (0, 102, 204), (ball_x,ball_y), 25)
        pygame.display.update()

        if player_1_y >= 530:
            player_1_y = 530
            play_1_y_change = 0
        if player_1_y <= 60:
            play_1_y_change = 0
            player_1_y = 60

        if player_2_y >= 530:
            player_2_y = 530
            play_2_y_change = 0
        if player_2_y <= 60:
            player_2_y = 60
            play_2_y_change = 0


        if b == 0: #R_Down
            ball_x += ball_x_change
            ball_y += ball_y_change
        if b == 1: #R_Up
            ball_x += ball_x_change
            ball_y -= ball_y_change
        if player_1_y <= ball_y <= player_1_y + 150 and ball_x == player_1_x + 25:
            po = 'Right'
            b = random.randint(0,1)
        if player_2_y <= ball_y <= player_2_y + 150 and ball_x == player_2_x:
            po = 'Left'
            b = random.randint(3,4)
        if b == 3: #l_down
            ball_x -= ball_x_change
            ball_y += ball_y_change
            ball_x_change = 1
            ball_y_change = 1
        if b == 4 : #l_up
            ball_x -= ball_x_change
            ball_y -= ball_y_change
            ball_x_change = 1
            ball_y_change = 1
        if ball_y <= 80:
            if po == "Right":
                b = 0 
            if po == "Left":
                b = 3
        if ball_y >= 655:
            if po == 'Right':
                b = 1
            if po == 'Left':
                b = 4

        if ball_x >= dx - 20:
            win_left()
        if ball_x <= 20:
            win_right()

    pygame.quit()

def option():
    op_white = 255,255,255
    option_title = f_arial(50).render("Options", True, (255, 255, 255))
    op_version_text = f_arial(20).render("Version: 1 beta 1", True, (255,255,255))
    op_theme_text = f_arial(40).render("Theme", True, (255,255,255))
    op_theme_text_lg = f_arial(40).render("< Choose Theme for Game >", True, (255,255,255))
    while True:
        op_back_text = f_arial(25).render("<< Back", True, (op_white))
        pos_op = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pos_op)
                if 0 <= pos_op[0] <= 80 and 0 <= pos_op[1] <= 30:
                    op_white = 0, 204, 255
                if 100 <= pos_op[0] <= 980 and 100 <= pos_op[1] <= 150:
                    option_theme()

            if event.type == pygame.MOUSEBUTTONUP:
                op_white = 255,255,255
                if 0 <= pos_op[0] <= 80 and 0 <= pos_op[1] <= 30:
                    main()

        display.fill((df_bg_color))
        display.blit(bg_se,(0,0))
        pygame.draw.rect(display,(0, 102, 204) ,(0,0,dx,50))
        display.blit(option_title, (470,0))
        display.blit(op_back_text,(5,5))
        display.blit(op_version_text, (2,655))
        pygame.draw.rect(display,(155,155,155), (100, 100, 880, 50))
        display.blit(op_theme_text, (100,100))
        display.blit(op_theme_text_lg, (400, 100))
        pygame.display.update()

    pygame.quit()
def option_theme():
    option_theme_title = f_arial(50).render("Options > Theme", True, (255, 255, 255))
    option_theme_white = 255,255,255
    option_theme_select = f_arial(40).render("Selected:", True, (255,255,255))
    option_theme_snt_text = f_arial(40).render("Select new theme:", True, (255,255,255))
    while True:
        option_theme_back_text = f_arial(25).render("<< Back", True, (option_theme_white))
        pos_op_theme = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pos_op_theme)
                if 0 <= pos_op_theme[0] <= 80 and 0 <= pos_op_theme[1] <= 30:
                    option_theme_white = 0, 204, 255
            if event.type == pygame.MOUSEBUTTONUP:
                option_theme_white = 255,255,255
                if 0 <= pos_op_theme[0] <= 80 and 0 <= pos_op_theme[1] <= 30:
                    option()
                if 140 <= pos_op_theme[0] <= 340 and 300 <= pos_op_theme[1] <= 400:
                    with open('Options/bg.json', 'w') as f:
                        json.dump(1, f)
                    bg_se = bg01
                    os.execl(sys.executable, sys.executable, *sys.argv)
                    option_theme()
                if 390 <= pos_op_theme[0] <= 590 and 300 <= pos_op_theme[1] <= 400:
                    with open('Options/bg.json', 'w') as f:
                        json.dump(2, f)
                    bg_se = bg02
                    os.execl(sys.executable, sys.executable, *sys.argv)
                    option_theme()

        display.fill((155,155,155))
        pygame.draw.rect(display,(0, 102, 204) ,(0,0,dx,50))
        display.blit(option_theme_back_text,(5,5))
        display.blit(option_theme_title,(390,0))
        display.blit(option_theme_select, (100,100))
        bgs01 = pygame.image.load('bg.jpg')
        bgs01 = pygame.transform.scale(bgs01, (200,100))
        bgs02 = pygame.image.load('Asset/background/bg-01.png')
        bgs02 = pygame.transform.scale(bgs02, (200,100))
        bgs03 = pygame.image.load('Asset/background/bg-02.jpg')
        bgs03 = pygame.transform.scale(bgs03, (200,100))
        bgs_se = bgs01
        if bgcs == 1:
            bgs_se = bgs01
            bgs_se = pygame.transform.scale(bgs_se,(200,100))
        if bgcs == 2:
            bgs_se = bgs02
            bgs_se = pygame.transform.scale(bgs_se,(200,100))
        display.blit(bgs_se, (130, 150))
        display.blit(option_theme_snt_text, (100, 250))
        display.blit(bgs01, (140, 300))
        display.blit(bgs02, (390, 300))
        pygame.display.update()
    pygame.quit()
def win_left():
    win_text = f_arial(60).render("Left Win", True, (255,255,255))
    w_star = pygame.image.load('Asset/win.png')
    main_menu_text = f_arial(30).render("Back to Main Menu", True, (255,255,255))
    while True:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if 410 <= pos[0] <= 680 and 400 <= pos[1] <= 500:
                    main() 

        display.blit(bg_se, (0,0))
        pygame.draw.rect(display, (51, 153, 255), (340,10, 400, 650))
        display.blit(win_text, (453,190))
        display.blit(w_star, (340, -20))
        pygame.draw.rect(display, (0, 102, 204), (410, 400, 270, 100))
        display.blit(main_menu_text, (440,430))
        pygame.display.update()
def win_right():
    win_text = f_arial(60).render("Right Win", True, (255,255,255))
    w_star = pygame.image.load('Asset/win.png')
    main_menu_text = f_arial(30).render("Back to Main Menu", True, (255,255,255))
    while True:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if 410 <= pos[0] <= 680 and 400 <= pos[1] <= 500:
                    main() 

        display.blit(bg_se, (0,0))
        pygame.draw.rect(display, (51, 153, 255), (340,10, 400, 650))
        display.blit(win_text, (450,190))
        display.blit(w_star, (340, -20))
        pygame.draw.rect(display, (0, 102, 204), (410, 400, 270, 100))
        display.blit(main_menu_text, (440,430))
        pygame.display.update()
def loading():
    loading = pygame.image.load("logo_g.png")
    loading_text = f_arial(25).render("loading", True, (255,255,255))
    while True:
        lpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                print(lpos)

        display.blit(loading, (340,240))
        display.blit(loading_text, (504.5,400))
        pygame.display.update()
        sleep(2)
        main()
    pygame.quit()
loading()