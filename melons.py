"""Classes for melon orders."""

from random import randint


class AbstractMelonOrder(object):
    """Parent code for all types of melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """ implements dynamic algorithm """
        self.base_price = randint(5, 9)
        return self.base_price

    def get_total(self):
        """Calculate price, including tax."""
        base = self.get_base_price()
        print base
        if self.species.lower == "christmas":
            base *= 1.5

        total = (1 + self.tax) * self.qty * base

        if self.qty < 10 and self.order_type == "international":
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True




class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.order_type = "government"
        self.passed_inspection = False
        self.tax = 0

    def mark_inspection(self, passed):

        if passed is True:
            passed_inspection = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
