from .base import BasePlayer


class PlayerCautious(BasePlayer):
    '''
    The cautious player buys any property
    if he keeps at leats 80 of money
    after the purchase.
    '''
    def _roles_to_payment(self, patrimony):
        if (self.money - patrimony.property_price) >= 80:
            self.paid(patrimony.property_price, patrimony.type_of_behavior)
            return True
        return False
