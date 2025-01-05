import pygame
import sys
import os

from poker import PokerGame

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60
BACKGROUND_COLOR = (34, 139, 34)  # Green for the poker table

# Asset paths
ASSETS_DIR = "assets"

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Poker Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Load card images
def load_card_images():
    """Loads all card images from the assets directory."""
    card_images = {}
    for filename in os.listdir(ASSETS_DIR):
        if filename.endswith(".png"):
            card_name = filename.split(".")[0]  # Extract '2c', 'Th', etc.
            image_path = os.path.join(ASSETS_DIR, filename)
            card_images[card_name] = pygame.image.load(image_path)
    return card_images


# Load images
card_images = load_card_images()
card_back_image = card_images.get("back", None)

# Scale card images to a standard size
CARD_WIDTH = 50
CARD_HEIGHT = 70
for key in card_images:
    card_images[key] = pygame.transform.scale(card_images[key], (CARD_WIDTH, CARD_HEIGHT))


def draw_poker_table():
    """Draws the poker table and placeholders for cards and chips."""
    # Draw a large oval for the poker table
    table_rect = pygame.Rect(100, 100, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200)
    pygame.draw.ellipse(screen, (0, 100, 0), table_rect)

    # Draw placeholders for community cards
    community_card_positions = [(250 + i * 80, 250) for i in range(5)]
    for pos in community_card_positions:
        if card_back_image:
            screen.blit(card_back_image, pos)

    # Draw placeholders for player hands
    player_card_positions = [
        [(200, 450), (260, 450)],  # Player 1 cards
        [(200, 50), (260, 50)],   # Player 2 cards
    ]
    for player_cards in player_card_positions:
        for pos in player_cards:
            if card_back_image:
                screen.blit(card_back_image, pos)


def main():
    """Main game loop."""
    poker_game = PokerGame()

    while poker_game.game_is_live:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                poker_game.game_is_live = False

        # Clear screen
        screen.fill(BACKGROUND_COLOR)

        # Draw poker table
        draw_poker_table()

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
