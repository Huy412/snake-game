import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (238, 0, 0)
green = (0, 139, 0)
blue = (50, 153, 213)
orange = (238, 118, 0)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 20)
custom_font = pygame.font.Font("SAIGON1985.ttf", 48)

pygame.mixer.music.load('bg.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


def score_func(score):
    value = custom_font.render("Score : " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def snake_func(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])

def yummy_func():
    print('Yummy!!')
    return


def message_func(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLooping_func():
    game_end = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_end:

        while game_close == True:
            dis.fill(blue)
            font = pygame.font.SysFont('inkfree', 40)
            title = font.render('Game Over', True, black )
            restart_button = font.render('R - Restart', True, (255, 255, 255))
            quit_button = font.render('Q - Quit', True, (255, 255, 255))
            dis.blit(title, (dis_width / 2 - title.get_width() / 2, dis_height / 2 - title.get_height() / 3))
            dis.blit(restart_button,(dis_width / 2 - restart_button.get_width() / 2, dis_height / 1.9 + restart_button.get_height()))
            dis.blit(quit_button,(dis_width / 2 - quit_button.get_width() / 2, dis_height / 2 + quit_button.get_height() / 2))

            # Thực hiện điểm số của trò chơi tương đương với chiều dài của con rắn - 1 (không tính phần đầu
            # của con rắn)
            score_func(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_end = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLooping_func()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        pygame.draw.rect(dis, orange, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake_func(snake_block, snake_List)
        score_func(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            yummy_func()
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameLooping_func()
