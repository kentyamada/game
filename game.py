import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Create the car object
car = pygame.Rect(screen_width // 2 - 25, screen_height - 100, 50, 100)
car_color = (150, 230, 0)
car_speed = 5

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.x -= car_speed
    if keys[pygame.K_RIGHT]:
        car.x += car_speed

    # Keep car within screen boundaries
    if car.left < 0:
        car.left = 0
    if car.right > screen_width:
        car.right = screen_width

    # Draw the game objects
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, car_color, car)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
