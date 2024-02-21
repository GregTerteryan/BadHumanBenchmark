import pygame
import sys
import random
import time

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 36
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming is fun and challenging.",
    "Pygame makes game development enjoyable.",
    "Practice makes perfect.",
    "Type as fast as you can!",
    "You don't know what you're getting into.",
    "It should've been me! Not him! It's not fair!",
    "It's free real estate."
]

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Test")
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

def show_sentence(sentence):
    text = font.render(sentence, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text, text_rect)

def show_menu():
    menu_text = font.render("Press SPACE to start typing", True, WHITE)
    menu_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(menu_text, menu_rect)

def show_results(wpm, accuracy):
    result_text = font.render(f"WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%", True, WHITE)
    result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
    screen.blit(result_text, result_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Display results for 3 seconds

def main():
    start_menu = True
    sentence = random.choice(SENTENCES)
    input_text = ""
    start_time = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif start_menu and event.key == pygame.K_SPACE:
                    start_menu = False
                    start_time = time.time()
                elif not start_menu:
                    if event.key == pygame.K_RETURN:
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        words_per_minute = (len(input_text.split()) / elapsed_time) * 60
                        accuracy = sum(a == b for a, b in zip(sentence, input_text)) / len(sentence) * 100

                        show_results(words_per_minute, accuracy)

                        # Restart the game
                        start_menu = True
                        sentence = random.choice(SENTENCES)
                        input_text = ""
                        start_time = None
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.unicode.isprintable():
                        input_text += event.unicode

        screen.fill(BLACK)

        if start_menu:
            show_menu()
        else:
            show_sentence(sentence)

            input_text_surface = font.render(input_text, True, WHITE)
            input_rect = input_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(input_text_surface, input_rect)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
