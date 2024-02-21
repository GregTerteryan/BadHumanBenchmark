import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 36
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Words for the memory test
word_list = ["Apple", "Banana", "Cherry", "Orange", "Grape", "Lemon", "Mango", "Peach", "Pear", "Plum"]

# Function to display text
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to run the memory test
def verbal_memory_test():
    score = 0
    while True:
        # Display instructions
        screen.fill(BLACK)
        display_text("Memorize the words!", font_large, WHITE, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        time.sleep(2)  # Display instructions for 2 seconds

        # Display words for 5 seconds
        screen.fill(BLACK)
        pygame.display.flip()
        time.sleep(0.5)  # Short pause before displaying words
        word_sequence = random.sample(word_list, score + 1)
        for word in word_sequence:
            screen.fill(BLACK)  # Clear the screen before displaying each word
            display_text(word, font_large, WHITE, WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()
            time.sleep(1)

        # Clear the screen
        screen.fill(BLACK)
        pygame.display.flip()
        time.sleep(1)  # Pause before user input

        # User input phase
        user_input = []
        for word in word_sequence:
            screen.fill(BLACK)  # Clear the screen before displaying user input instructions
            display_text("Type: " + word, font_small, WHITE, WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()

            # Get user input
            input_word = ""
            looping = True
            while looping:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            looping = False
                            break
                        elif event.key == pygame.K_BACKSPACE:
                            input_word = input_word[:-1]
                        elif event.unicode.isalpha():
                            input_word += event.unicode.upper()

                screen.fill(BLACK)
                display_text("Type: " + input_word, font_small, WHITE, WIDTH // 2, HEIGHT // 2)
                pygame.display.flip()

            user_input.append(input_word)

        # Compare user input with the original sequence
        correct = sum([1 for user_word, original_word in zip(user_input, word_sequence) if user_word == original_word.upper()])

        # Display result
        screen.fill(BLACK)
        display_text(f"You got {correct}/{len(word_sequence)} correct!", font_large, WHITE, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        time.sleep(3)

        if correct == len(word_sequence):
            score += 1
        else:
            break

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Verbal Memory Human Benchmark Test")
clock = pygame.time.Clock()

# Set up fonts
font_large = pygame.font.Font(None, FONT_SIZE * 2)
font_small = pygame.font.Font(None, FONT_SIZE)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                verbal_memory_test()

    screen.fill(BLACK)
    display_text("Press SPACE to start the test", font_large, WHITE, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()

    clock.tick(FPS)

# Quit Pygame
pygame.quit()
