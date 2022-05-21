import random
import unittest

# CS-362- Random Testing Hands On

from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def test1(self):
            Visa = random.randint(4000000000000000, 4999999999999999)
            credit_card_validator(Visa)

    def test2(self):
            master_card = random.randint(5100000000000000, 5599999999999999)
            credit_card_validator(master_card)

    def test3(self):
            master_card = random.randint(2221000000000000, 2720999999999999)
            credit_card_validator(master_card)

    def test4(self):
            american_express = random.randint(340000000000000, 379999999999999)
            credit_card_validator(american_express)

    def test5(self):
            cardNumber = random.randint(0000000000000000, 9999999999999999)
            credit_card_validator(cardNumber)


if __name__ == '__main__':
    unittest.main()
