from random import randint

from .base import BasePlayer


class PlayerRandom(BasePlayer):
    '''
    The random player buys any property
    in which he stop with the probability
    of 50%.
    '''
    def _roles_to_payment(self, patrimony):
        if randint(0, 1) > 0:
            self.paid(patrimony.property_price, patrimony.type_of_behavior)
            return True
        return False
