class Partner:

    def __init__(self,
                 partner_id,
                 partner_type,
                 name,
                 director,
                 email,
                 phone,
                 address,
                 inn,
                 rating,
                 discount=0
                 ):
        self.partner_id = partner_id
        self.partner_type = partner_type
        self.partner_name = name
        self.partner_director = director
        self.partner_email = email
        self.partner_phone = phone
        self.partner_address = address
        self.partner_inn = inn
        self.partner_rating = rating
        self.partner_discount = discount


class Sale:

    def __init__(self, partner, total_price):
        self.partner = partner
        self.total_price = total_price
