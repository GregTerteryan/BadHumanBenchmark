import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Time Test")
clock = pygame.time.Clock()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main():
    running = True
    font = pygame.font.Font(None, 36)

    while running:
        screen.fill(WHITE)
        draw_text("Press space when the color changes", font, BLACK, WIDTH // 2, HEIGHT // 4)

        # Check if space bar is pressed before the screen changes
        space_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_pressed = True

        pygame.display.flip()
        pygame.time.wait(random.randint(1000, 5000)) # Wait for random time between 1 and 5 seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_pressed = True
                screen.fill(BLACK)
                draw_text("Too early! Try again.", font, WHITE, WIDTH // 2, HEIGHT // 2 + 50)
                pygame.display.flip()
                pygame.time.wait(2000)

        if not space_pressed:
            screen.fill(BLACK)
            draw_text("NOW!", font, WHITE, WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()

            # Record the start time after displaying "NOW!"
            start_time = time.time()

            # Wait for user input (pressing space)
            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting_for_input = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        end_time = time.time()
                        reaction_time = end_time - start_time
                        draw_text(f"Your reaction time: {reaction_time:.3f} seconds", font, WHITE, WIDTH // 2, HEIGHT // 2 + 50)
                        pygame.display.flip()
                        pygame.time.wait(2000)  # Show the reaction time for 2 seconds
                        waiting_for_input = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
