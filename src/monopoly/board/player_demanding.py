from .base import BasePlayer


class PlayerDemanding(BasePlayer):
    '''
    The demanding player buys any property
    since the rent price is higher than 50.
    '''
    def _roles_to_payment(self, patrimony):
        if patrimony.rental_price > 50:
            self.paid(patrimony.property_price, patrimony.type_of_behavior)
            return True
        return False
