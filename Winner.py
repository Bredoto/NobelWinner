def get_year(self):
    return self.year


def get_category(self):
    return self.category


def get_prize(self):
    return self.prize


def get_motivation(self):
    return self.motivation


def get_prizeshare(self):
    return self.prizeshare


def get_laureateid(self):
    return self.laureateid


def get_laureatetype(self):
    return self.laureatetype


def get_fullname(self):
    return self.fullname


def get_birthdate(self):
    return self.birthdate


def get_birthcity(self):
    return self.birthcity


def get_birthcountry(self):
    return self.birthcountry


def get_sex(self):
    return self.sex


def get_organizationname(self):
    return self.organizationname


def get_organizationcity(self):
    return self.organizationcity


def get_organizationcountry(self):
    return self.organizationcountry


def get_deathdate(self):
    return self.deathdate


def get_deathcity(self):
    return self.deathcity


def get_deathcountry(self):
    return self.deathcountry


class Winner:
    def __init__(self, year, category, prize, motivation, prizeshare, laureateid, laureatetype, fullname, birthdate,
                 birthcity, birthcountry, sex, organizationname, organizationcity, organizationcountry, deathdate,
                 deathcity, deathcountry):
        self.year = year
        self.category = category
        self.prize = prize
        self.motivation = motivation
        self.prizeshare = prizeshare
        self.laureateid = laureateid
        self.laureatetype = laureatetype
        self.fullname = fullname
        self.birthdate = birthdate
        self.birthcity = birthcity
        self.birthcountry = birthcountry
        self.sex = sex
        self.organizationname = organizationname
        self.organizationcity = organizationcity
        self.organizationcountry = organizationcountry
        self.deathdate = deathdate
        self.deathcity = deathcity
        self.deathcountry = deathcountry
