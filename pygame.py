import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 640, 480
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Define snake properties
snake_block = 10
snake_speed = 15

# Set up clock
clock = pygame.time.Clock()

# Define font
font_style = pygame.font.SysFont("bahnschrift", 25)

def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, red)
    game_display.blit(value, [0, 0])

def game_loop():
    # Game variables
    game_over = False
    game_close = False

    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    # Food coordinates
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            game_display.fill(black)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)

        # Draw food
        pygame.draw.rect(game_display, green, [foodx, foody, snake_block, snake_block])

        # Snake movement
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for block in snake_list:
            pygame.draw.rect(game_display, white, [block[0], block[1], snake_block, snake_block])

        display_score(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
