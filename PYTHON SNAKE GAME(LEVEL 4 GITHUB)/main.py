
import pygame
import random
import sys
import os

pygame.init()
pygame.mixer.init()

# Screen
WIDTH, HEIGHT = 800, 600
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEON SNAKE - ARCADE")

clock = pygame.time.Clock()

# Colors
BG = (10, 10, 25)
GREEN = (0, 255, 130)
NEON = (0, 220, 255)
RED = (255, 60, 80)
GOLD = (255, 200, 0)
WHITE = (255, 255, 255)
GRAY = (130, 130, 150)

# Fonts
font = pygame.font.SysFont("consolas", 25, bold=True)
big_font = pygame.font.SysFont("consolas", 55, bold=True)
small_font = pygame.font.SysFont("consolas", 18)

# Game area
GAME_RECT = pygame.Rect(20, 80, 760, 500)

# High score
HIGH_SCORE_FILE = "snake_highscore.txt"

def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))

high_score = load_high_score()

# Food generator
def new_food(snake):
    while True:
        pos = (
            random.randrange(1, 39) * CELL,
            random.randrange(5, 29) * CELL
        )
        if pos not in snake:
            return pos

# Reset game
def reset_game():
    snake = [(400, 300), (380, 300), (360, 300)]
    return {
        "snake": snake,
        "direction": (CELL, 0),
        "food": new_food(snake),
        "gold_food": None,
        "score": 0,
        "speed": 10,
        "food_count": 0,
        "state": "playing"
    }

game = reset_game()

# Drawing helpers
def draw_text(text, fnt, color, x, y, center=True):
    surface = fnt.render(text, True, color)
    rect = surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(surface, rect)

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect, border_radius=12)
    pygame.draw.rect(screen, WHITE, rect, 2, border_radius=12)
    draw_text(text, font, WHITE, rect.centerx, rect.centery)

def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (20, 25, 45), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, (20, 25, 45), (0, y), (WIDTH, y))

def draw_snake(snake):
    for i, part in enumerate(snake):
        rect = pygame.Rect(part[0], part[1], CELL, CELL)
        color = NEON if i == 0 else GREEN
        pygame.draw.rect(screen, color, rect, border_radius=6)

        if i == 0:
            pygame.draw.circle(
                screen, WHITE,
                (part[0] + 6, part[1] + 6), 3
            )
            pygame.draw.circle(
                screen, WHITE,
                (part[0] + 15, part[1] + 6), 3
            )

def draw_food(pos, color):
    pygame.draw.circle(
        screen, color,
        (pos[0] + CELL // 2, pos[1] + CELL // 2),
        CELL // 2 - 2
    )

# Menu
def main_menu():
    screen.fill(BG)
    draw_grid()

    draw_text("NEON SNAKE", big_font, NEON, 400, 180)
    draw_text("ULTIMATE ARCADE EDITION", font, WHITE, 400, 235)

    draw_button(
        "START GAME",
        pygame.Rect(290, 320, 220, 55),
        (0, 130, 100)
    )

    draw_text(
        "Arrow Keys: Move | P: Pause | ESC: Menu",
        small_font, GRAY, 400, 430
    )

    draw_text(
        f"High Score: {high_score}",
        font, GOLD, 400, 480
    )

# Game loop
running = True
menu_button = pygame.Rect(290, 320, 220, 55)

while running:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                game["state"] = "menu"

            if game["state"] == "playing":

                if event.key == pygame.K_UP and game["direction"] != (0, CELL):
                    game["direction"] = (0, -CELL)

                elif event.key == pygame.K_DOWN and game["direction"] != (0, -CELL):
                    game["direction"] = (0, CELL)

                elif event.key == pygame.K_LEFT and game["direction"] != (CELL, 0):
                    game["direction"] = (-CELL, 0)

                elif event.key == pygame.K_RIGHT and game["direction"] != (-CELL, 0):
                    game["direction"] = (CELL, 0)

                elif event.key == pygame.K_p:
                    game["state"] = "paused"

            elif game["state"] == "paused":
                if event.key == pygame.K_p:
                    game["state"] = "playing"

            elif game["state"] == "gameover":
                if event.key == pygame.K_r:
                    game = reset_game()

                elif event.key == pygame.K_m:
                    game["state"] = "menu"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game["state"] == "menu":
                if menu_button.collidepoint(mouse_pos):
                    game = reset_game()

    # MENU
    if game["state"] == "menu":
        main_menu()

    # PLAYING
    elif game["state"] == "playing":

        screen.fill(BG)
        draw_grid()

        snake = game["snake"]
        dx, dy = game["direction"]

        head = (
            snake[0][0] + dx,
            snake[0][1] + dy
        )

        grow = head == game["food"] or head == game["gold_food"]

        # Wall collision
        if not GAME_RECT.collidepoint(head) or (
            head[0] < GAME_RECT.left or
            head[1] < GAME_RECT.top
        ):
            game["state"] = "gameover"

        # Self collision
        elif head in (snake if grow else snake[:-1]):
            game["state"] = "gameover"

        else:
            snake.insert(0, head)

            if head == game["food"]:
                game["score"] += 10
                game["food_count"] += 1
                game["food"] = new_food(snake)

                if game["food_count"] % 5 == 0:
                    game["gold_food"] = new_food(snake)

                game["speed"] = min(25, 10 + game["food_count"] // 3)

            elif head == game["gold_food"]:
                game["score"] += 50
                game["gold_food"] = None

            else:
                snake.pop()

        # High score update
        if game["score"] > high_score:
            high_score = game["score"]
            save_high_score(high_score)

        # Draw
        draw_snake(snake)
        draw_food(game["food"], RED)

        if game["gold_food"]:
            draw_food(game["gold_food"], GOLD)

        draw_text(
            f"SCORE: {game['score']}",
            font, WHITE, 30, 25, False
        )

        draw_text(
            f"BEST: {high_score}",
            font, GOLD, 340, 25, False
        )

        draw_text(
            f"SPEED: {game['speed']}",
            font, NEON, 620, 25, False
        )

    # PAUSED
    elif game["state"] == "paused":
        screen.fill(BG)
        draw_grid()
        draw_snake(game["snake"])
        draw_text("PAUSED", big_font, GOLD, 400, 250)
        draw_text("Press P to Resume", font, WHITE, 400, 320)

    # GAME OVER
    elif game["state"] == "gameover":
        screen.fill(BG)
        draw_grid()

        draw_text("GAME OVER", big_font, RED, 400, 200)
        draw_text(
            f"Your Score: {game['score']}",
            font, WHITE, 400, 280
        )
        draw_text(
            f"High Score: {high_score}",
            font, GOLD, 400, 330
        )
        draw_text("R = Restart", font, GREEN, 400, 400)
        draw_text("M = Main Menu", font, NEON, 400, 450)

    pygame.display.flip()

    if game["state"] == "playing":
        clock.tick(game["speed"])
    else:
        clock.tick(30)

pygame.quit()
sys.exit()


