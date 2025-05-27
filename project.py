import pygame
import time
import random

pygame.init()

# Height and width display
display_width = 800
display_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
blue = (63, 162, 246)
mypink = (255, 144, 188)
peorple = (200, 161, 224)
bright_pink = (230, 120, 170)

gameDisplay = pygame.display.set_mode((display_width, display_height))

# Game title
pygame.display.set_caption('My Game')

# Frame per second on display
clock = pygame.time.Clock()

# Load image
pigimg = pygame.image.load('images/pig.png')
pig_width = 48

# Load obstacle images
images = [
    pygame.image.load('images/lemon.png'),
    pygame.image.load('images/cabbage.png'),
    pygame.image.load('images/corn.png'),
    pygame.image.load('images/eggplant.png'),
    pygame.image.load('images/mushroom.png'),
    pygame.image.load('images/potato.png'),
    pygame.image.load('images/broccoli.png'),
    pygame.image.load('images/carrot.png'),
    pygame.image.load('images/sweetpepper.png'),
    pygame.image.load('images/sweetpepper2.png')
]


def button(msg, x, y, width, height, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "play":
                main()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, width, height))

    smallText = pygame.font.Font("freesansbold.ttf", 17)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))
    gameDisplay.blit(TextSurf, TextRect)


def quitgame():
    pygame.quit()
    quit()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(peorple)
        largeText = pygame.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_objects("Let's Play My Game", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Start", 150, 450, 100, 50, bright_pink, mypink, "play")
        button("Quit", 550, 450, 100, 50, red, bright_red, "quit")

        pygame.display.update()


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, red)
    gameDisplay.blit(text, (0, 0))


def things(things_x, things_y, image):
    gameDisplay.blit(image, (things_x, things_y))


def pig(x, y):
    gameDisplay.blit(pigimg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    main()


def crash():
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects("You Lose", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, bright_pink, mypink, main)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()


def main():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    things_start_x = random.randrange(0, display_width)
    things_start_y = -700
    things_speed = 7
    things_width = 50
    things_height = 50

    dodged = 0
    selected_image = random.choice(images)

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(peorple)

        things(things_start_x, things_start_y, selected_image)
        things_start_y += things_speed

        things_dodged(dodged)
        pig(x, y)

        if x > display_width - pig_width or x < 0:
            crash()

        if things_start_y > display_height:
            things_start_y = 0 - things_height
            things_start_x = random.randrange(0, display_width)
            dodged += 1
            things_speed += 1
            selected_image = random.choice(images)

        if y < things_start_y + things_height:
            if x > things_start_x and x < things_start_x + things_width or x + pig_width > things_start_x and x + pig_width < things_start_x + things_width:
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
main()
pygame.quit()
quit()
