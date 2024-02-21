import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Visual Memory Test")
clock = pygame.time.Clock()

# Function to display text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to run the visual memory test
def visual_memory_test(sequence_length):
    global running
    sequence = []
    user_sequence = []
    font = pygame.font.Font(None, FONT_SIZE)

    # Generate a random sequence
    for _ in range(sequence_length):
        sequence.append(random.randint(1, 9))

    # Display the sequence to the player
    for num in sequence:
        screen.fill(BLACK)
        draw_text(str(num), font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        pygame.time.delay(1000)  # Display each number for 1 second

    # Clear the screen
    screen.fill(BLACK)
    pygame.display.flip()

    # Get the player's input
    for _ in range(sequence_length):
        user_input = None
        while user_input is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        user_input = event.key - pygame.K_0

        user_sequence.append(user_input)

        # Display the user's input without delay
        screen.fill(BLACK)
        draw_text(str(user_input), font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.flip()

    # Compare the sequences
    if user_sequence == sequence:
        return True
    else:
        return False

# Main game loop
running = True
sequence_length = 1

while running:
    font = pygame.font.Font(None, FONT_SIZE)  # Initialize font here
    screen.fill(BLACK)
    draw_text(f"Press Space to start the Visual Memory Test ({sequence_length} numbers)", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if visual_memory_test(sequence_length):
                sequence_length += 1
            else:
                sequence_length = 1  # Restart at one number if the guess is incorrect

    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
