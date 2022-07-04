from .base import BasePlayer


class PlayerImpulsive(BasePlayer):
    '''
    The impulsive player buys any
    property in which he stop.
    '''
    def _roles_to_payment(self, patrimony):
        self.paid(patrimony.property_price, patrimony.type_of_behavior)
        return True
