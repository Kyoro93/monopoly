from monopoly.config import settings

from monopoly.board.factory import create_board
from monopoly.board.game_statistics import show_statistics


def main():
    '''
    Runs a program that simulate 300 games and
    print their results on console.
    '''
    results = []
    # For each simulation
    for index in range(int(settings.ENV_NUMBER_SIMULATION)):
        # Create a new board
        board = create_board()
        # While theres is no winner, continues playing
        while board.winner is None:
            for player in board.players:
                # Verify if player entered bankruptcy and
                # remove him from the game
                if player.gameover:
                    board.remove(player)

                # Checks for the winner
                winner = board.check_winner(player)

                # If there's a winner, ends game
                if winner:
                    board.winner = winner
                    break
                # Else keep playing
                board.play(player, board)
            board.played += 1
        results.append(board.finish())
    show_statistics(results)


if __name__ == "__main__":
    main()
