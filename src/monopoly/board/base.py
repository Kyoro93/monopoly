from abc import ABC, abstractmethod

from monopoly.config import settings


class BasePlayer(ABC):

    def __init__(
        self, behavior, position=0,
        money=settings.ENV_PLAYER_MONEY
    ):
        self.position = position
        self.money = money
        self.behavior = behavior
        self.gameover = False

    def __str__(self):
        return f"{self.behavior}"

    def __repr__(self):
        return f"{self.behavior}"

    def income_or_sale(self, patrimony, board=None):
        if patrimony.type_of_behavior:
            if self != patrimony.type_of_behavior:
                self.paid(patrimony.rental_price, patrimony.type_of_behavior)
            return

        if self._roles_to_payment(patrimony):
            patrimony.type_of_behavior = self

    @abstractmethod
    def _roles_to_payment(self, patrimony, board):
        raise NotImplementedError()

    def paid(self, property_price, type_of_behavior=None):
        self.money -= property_price
        if type_of_behavior:
            type_of_behavior.money += property_price
        if not self.money:
            self.gameover = True
