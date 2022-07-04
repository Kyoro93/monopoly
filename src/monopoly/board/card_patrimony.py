from random import randint


class Patrimony:

    def __init__(self, id, type_of_behavior=None, *args, **kwargs):
        self.id = id
        self.type_of_behavior = type_of_behavior
        self.rental_price = randint(30, 120)
        self.property_price = randint(30, 120)

    def __repr__(self):
        return f'''
            id:{self.id}
            type_of_behavior:{self.type_of_behavior}
            rental_price:{self.rental_price}
            property_price:{self.property_price}
        '''

    def __str__(self):
        return f'''
            id:{self.id}
            type_of_behavior:{self.type_of_behavior}
            rental_price:{self.rental_price}
            property_price:{self.property_price}
        '''
