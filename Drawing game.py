import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Drawing Game with Erase Option")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the drawing and erasing
drawing = False
erasing = False
last_pos = None

# Fill the screen with white
screen.fill(WHITE)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                if last_pos:
                    if erasing:
                        pygame.draw.line(screen, WHITE, last_pos, current_pos, 15)  # Erase by drawing white lines
                    else:
                        pygame.draw.line(screen, BLACK, last_pos, current_pos, 5)  # Draw with black color
                last_pos = current_pos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:  # Press E to toggle between drawing and erasing
                erasing = not erasing
                if erasing:
                    print("Erase mode: ON")
                else:
                    print("Erase mode: OFF")

    # Update the screen
    pygame.display.update()
