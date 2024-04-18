import pygame
import sys
import random

pygame.init()

# Set the dimensions of the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jet Attack")

# Load the images
background_images = ["bg.jpg", "bg1.jpg"]  # List of house background images
current_background_index = 0

jet_img = pygame.image.load("jet.png")
jet_img = pygame.transform.scale(jet_img, (280, 280))  # Resize the jet image
jet_rect = jet_img.get_rect()

boom_img = pygame.image.load("boom.png")
boom_img = pygame.transform.scale(boom_img, (45, 70))  # Resize the boom image
boom_rect = boom_img.get_rect()

# Function to randomly place the jet on the screen
def place_jet():
    jet_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

place_jet()  # Place the jet initially

# Initialize dropped variable
dropped = False

# Initialize score
score = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not dropped:
                    boom_rect.center = jet_rect.center
                    dropped = True
            elif event.key == pygame.K_RETURN:  # Change background when Enter key is pressed
                current_background_index = (current_background_index + 1) % len(background_images)
                background_img = pygame.image.load(background_images[current_background_index]).convert()
                background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
                place_jet()  # Place the jet randomly when changing background
                dropped = False  # Reset dropped status
                score += 1  # Increment score when background changes

    # Move the jet
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jet_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        jet_rect.x += 5
    if keys[pygame.K_UP]:
        jet_rect.y -= 5
    if keys[pygame.K_DOWN]:
        jet_rect.y += 5

    # Ensure the jet stays within the screen bounds
    jet_rect.x = max(0, min(jet_rect.x, WIDTH - jet_rect.width))
    jet_rect.y = max(0, min(jet_rect.y, HEIGHT - jet_rect.height))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background image
    background_img = pygame.image.load(background_images[current_background_index]).convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    screen.blit(background_img, (0, 0))

    # Draw the jet
    screen.blit(jet_img, jet_rect)

    # Drop the boom if space bar is pressed
    if dropped:
        screen.blit(boom_img, boom_rect)
        boom_rect.y += 5  # Adjust the drop speed

        # Check if the boom is out of the screen
        if boom_rect.y > HEIGHT:
            dropped = False  # Reset dropped status
            current_background_index = (current_background_index + 1) % len(background_images)
            background_img = pygame.image.load(background_images[current_background_index]).convert()
            background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
            place_jet()  # Place the jet randomly when changing background
            score += 1  # Increment score when background changes

    # Draw the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (000, 000, 000))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()