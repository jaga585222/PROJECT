import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen and colors
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (242, 85, 96)
O_COLOR = (28, 170, 156)

# Set up the font for the 'X' and 'O'
font = pygame.font.SysFont('arial', 60)

# Initialize the game board
board = [None] * 9  # 3x3 grid flattened
current_player = 'X'

# Draw the grid
def draw_grid():
    screen.fill(WHITE)
    for row in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3 * row), (WIDTH, HEIGHT // 3 * row), 2)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3 * row, 0), (WIDTH // 3 * row, HEIGHT), 2)

# Draw the markers ('X' or 'O')
def draw_marks():
    for i, mark in enumerate(board):
        if mark:
            x = (i % 3) * (WIDTH // 3) + WIDTH // 6
            y = (i // 3) * (HEIGHT // 3) + HEIGHT // 6
            text = font.render(mark, True, X_COLOR if mark == 'X' else O_COLOR)
            screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

# Check if there's a winner
def check_winner():
    for i in range(3):
        # Check rows and columns
        if board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] is not None:
            return board[i*3]
        if board[i] == board[i+3] == board[i+6] and board[i] is not None:
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] is not None:
        return board[0]
    if board[2] == board[4] == board[6] and board[2] is not None:
        return board[2]
    
    # Check if there is a tie (board is full)
    if all([spot is not None for spot in board]):
        return 'Tie'
    
    return None

# Main game loop
def game_loop():
    global current_player

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // (HEIGHT // 3)
                col = x // (WIDTH // 3)
                idx = row * 3 + col

                # Place a mark if the space is available
                if board[idx] is None:
                    board[idx] = current_player

                    # Check for a winner
                    winner = check_winner()
                    if winner:
                        if winner == 'Tie':
                            print("It's a tie!")
                        else:
                            print(f"Player {winner} wins!")
                        pygame.time.wait(1500)  # Wait before closing
                        pygame.quit()
                        sys.exit()

                    # Switch players
                    current_player = 'O' if current_player == 'X' else 'X'

        # Draw the grid and marks
        draw_grid()
        draw_marks()

        # Update the display
        pygame.display.update()

# Run the game
if __name__ == "__main__":
    game_loop()
