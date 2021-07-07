import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

countdown = 10
font = pygame.font.Font("freesansbold.ttf", 32)

# Add while condition such that the countdown will run until it is greater than  0
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # render the number
    # paste the rendered number
    # decrease countdown by 1
    
    pygame.display.update()
    # Delay the program by 1

if countdown == 0:
    pygame.quit()
    sys.exit()
