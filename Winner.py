def get_year(self):
    return self.year


def get_category(self):
    return self.category


class Winner:
    def __init__(self, year, category, prize, motivation, prizeshare, laureateid, laureatetype, fullname):
        self.year = year
        self.category = category
        self.prize = prize
        self.motivation = motivation
        self.prizeshare = prizeshare
        self.laureateid = laureateid
        self.laureatetype = laureatetype
        self.fullname = fullname


