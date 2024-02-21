import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Benchmark Test Menu")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define font
font = pygame.font.Font(None, 36)

# Define menu options
menu_options = ["reaction_time", "typing", "verbal_memory", "visual_memory"]
selected_option = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if menu_options[selected_option] == "Exit":
                    pygame.quit()
                    sys.exit()
                else:
                    # Run the selected benchmark test
                    benchmark_test = menu_options[selected_option] + ".py"
                    exec(open(benchmark_test).read())
                    pygame.quit()
                    sys.exit()

    # Draw menu options
    screen.fill(black)
    for i, option in enumerate(menu_options):
        text = font.render(option, True, white if i == selected_option else black)
        text_rect = text.get_rect(center=(screen_width // 2, 200 + i * 50))
        screen.blit(text, text_rect)

    pygame.display.flip()
