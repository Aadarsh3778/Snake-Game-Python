import pygame
import random
pygame.mixer.init()

pygame.init()
game_window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Game (A.M)")

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
font = pygame.font.SysFont(None, 55)

def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    game_window.blit(screen_text, [x, y])

def plot(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

clock = pygame.time.Clock()


def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill((233, 210, 229))
        text_screen("Welcome to Snakes (A.M)", black, 60, 50)
        text_screen("Press Space To Play", green, 120, 220)
        text_screen("Press X To Exit", red, 120, 330)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("background.mp3")
                    pygame.mixer.music.play()
                    game_loop()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    exit_game = True

        pygame.display.update()
        clock.tick(60)


def game_loop():

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 15
    fps = 60
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(25, 480)
    food_y = random.randint(25, 480)
    food_size = 10
    score = 0
    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over:
            game_window.fill(white)
            text_screen("Game Over!Press Enter",  black, 80, 230)
            text_screen("Your Score: " + str(score * 25), black, 180, 180)
            text_screen("Press X To Exit", red, 170, 330)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("background.mp3")
                        pygame.mixer.music.play()
                        game_loop()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        exit_game = True

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = - 5
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = 5

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = - 5

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score = score + 1
                snake_length = snake_length + 5
                food_x = random.randint(25, 480)
                food_y = random.randint(25, 480)



            game_window.fill(black)
            text_screen("score: " + str(score * 25), red, 5, 5)
            pygame.draw.rect(game_window, white, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[: -1]:
                pygame.mixer.music.load("over.mp3")
                pygame.mixer.music.play()
                game_over = True

            if snake_x < 0 or snake_x > 600 or snake_y < 0 or snake_y > 600:
                pygame.mixer.music.load("over.mp3")
                pygame.mixer.music.play()
                game_over = True

            plot(game_window, red, snake_list, snake_size)

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome()
