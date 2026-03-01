import pygame
import random
import sys

pygame.init()

#Base
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Apple Collect')
clock = pygame.time.Clock()

#colors
yellow = (255, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#game over settings
game_over = False

#Lives
lives = 3

#Score
score = 0

#size
cart_x = 100
cart_y = 500
cart_speed = 17

apple_x = random.randint(0,WIDTH-100)
apple_y = 0
apple_speed = 5

bad_apple_x = random.randint(0,WIDTH-100)
bad_apple_y = -50
bad_apple_speed = 5




#Img
background = pygame.image.load('apple_img/apple_bg.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

cart_img = pygame.image.load('apple_img/collecter.png')
cart_img = pygame.transform.scale(cart_img, (100, 100))

apple_img = pygame.image.load('apple_img/apple.png')
apple_img = pygame.transform.scale(apple_img, (50, 50))

bad_apple_img = pygame.image.load('apple_img/bad_apple.png')
bad_apple_img = pygame.transform.scale(bad_apple_img, (50, 50))


#Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

    #draw
    screen.blit(background, (0, 0))
    screen.blit(cart_img, (cart_x, cart_y))
    screen.blit(apple_img, (apple_x, apple_y))
    screen.blit(bad_apple_img, (bad_apple_x, bad_apple_y))

    # Font score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, red)

    # Font lives
    text2 = font.render(f"Lives: {lives}", True, red)


    #Keys
    keys = pygame.key.get_pressed()

    if not game_over:

        if keys[pygame.K_d]:
            cart_x += apple_speed
        if keys[pygame.K_a]:
            cart_x -= apple_speed


        #Borders
        if cart_x < 0: cart_x = 0
        if cart_x > 700: cart_x = 700

        #Apple fall
        apple_y += apple_speed
        if apple_y > HEIGHT:
            apple_x = random.randint(0, WIDTH - 100)
            apple_y = 0

        #Bad Apple fall
        bad_apple_y += bad_apple_speed
        if bad_apple_y > HEIGHT:
            bad_apple_x = random.randint(0, WIDTH - 100)
            bad_apple_y = -50


        #Hit Box
        apple_rect = pygame.Rect(apple_x, apple_y, 50, 50)
        bad_apple_rect = pygame.Rect(bad_apple_x, bad_apple_y, 50, 50)
        cart_rect = pygame.Rect(cart_x, cart_y, 100, 100)


        #collision cart
        if cart_rect.colliderect(apple_rect):
            apple_x = random.randint(0, WIDTH - 100)
            apple_y = 0
            score += 1


        if cart_rect.colliderect(bad_apple_rect):
            bad_apple_x = random.randint(0, WIDTH - 100)
            bad_apple_y = 0
            lives -= 1


        # Font GameOver
        #game over text
        if lives < 0:
            game_over = True


    #Game over text
    if game_over == True:
        font2 = pygame.font.Font(None, 60)
        text_over = font2.render(f"Game Over \n press r to restart", True, red)
        screen.blit(text_over, (70, 300))

        #restart
        if keys[pygame.K_r]:
            game_over = False
            score = 0
            lives = 3
            apple_x = random.randint(0,WIDTH-100)
            apple_y = 0
            bad_apple_x = random.randint(0,WIDTH-100)
            bad_apple_y = -50


    #draw text
    screen.blit(text, (100, 25))
    screen.blit(text2, (500, 25))


    pygame.display.flip()
    clock.tick(60)