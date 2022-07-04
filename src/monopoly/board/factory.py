from monopoly.config import settings

from .game_board import GameBoard
from .player_cautious import PlayerCautious
from .player_demanding import PlayerDemanding
from .player_impulsive import PlayerImpulsive
from .player_random import PlayerRandom

strategies = {
    "impulsive": PlayerImpulsive,
    "demanding": PlayerDemanding,
    "cautious": PlayerCautious,
    "randomer": PlayerRandom,
}


def create_player(behavior: str, *args, **kwargs):
    try:
        return strategies[behavior](behavior=behavior, *args, **kwargs)

    except KeyError:
        available_strategies = ", ".join(strategies.keys())
        raise NotImplementedError(
            f"The player behavior '{behavior}' is not implemented."
            f"Please use the available strategies: {available_strategies}"
        )


def create_board():
    board = GameBoard()
    players = [
        create_player(behavior)
        for behavior in settings.ENV_behavior
    ]
    board.players = players
    return board
