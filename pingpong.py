import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
PLAYER_SPEED = 7
OPPONENT_SPEED = 6
BALL_SPEED = 7
FONT_SIZE = WIDTH // 20

# Setup display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")

# Fonts
FONT = pygame.font.SysFont("Consolas", FONT_SIZE)

# Clock
CLOCK = pygame.time.Clock()

# Player setup
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball setup
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = random.choice([BALL_SPEED, -BALL_SPEED]), random.choice([BALL_SPEED, -BALL_SPEED])

# Scores
player_score, opponent_score = 0, 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += PLAYER_SPEED

    # Opponent (enhanced AI) movement
    if opponent.centery < ball.centery and opponent.bottom < HEIGHT:
        opponent.y += OPPONENT_SPEED
    if opponent.centery > ball.centery and opponent.top > 0:
        opponent.y -= OPPONENT_SPEED

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_dx = -ball_dx

    # Ball out of bounds (scoring)
    if ball.left <= 0:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_dx, ball_dy = random.choice([BALL_SPEED, -BALL_SPEED]), random.choice([BALL_SPEED, -BALL_SPEED])
    if ball.right >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_dx, ball_dy = random.choice([BALL_SPEED, -BALL_SPEED]), random.choice([BALL_SPEED, -BALL_SPEED])

    # Drawing everything
    SCREEN.fill("black")
    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "white", opponent)
    pygame.draw.ellipse(SCREEN, "white", ball)
    pygame.draw.aaline(SCREEN, "white", (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw scores
    player_text = FONT.render(str(player_score), True, "white")
    opponent_text = FONT.render(str(opponent_score), True, "white")
    SCREEN.blit(player_text, (WIDTH // 2 + 20, 20))
    SCREEN.blit(opponent_text, (WIDTH // 2 - 40, 20))

    # Update the display
    pygame.display.flip()
    CLOCK.tick(60)
