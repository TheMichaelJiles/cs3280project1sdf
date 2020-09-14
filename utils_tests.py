#! /usr/bin/python
import unittest
import utils

class TestLuhnVerified(unittest.TestCase):
    def testAuthenticCardNumber(self):
        actual = 'Authentic'
        card_number = 30536723505217
        self.assertEqual(utils.luhn_verified(card_number), actual)
    def testFakeCardNumber(self):
        actual = 'Fake'
        card_number = 30536723505219
        self.assertEqual(utils.luhn_verified(card_number), actual)
    def testInvalidCardNumber(self):
        actual = 'N/A'
        card_number = '1234-1234'
        self.assertEqual(utils.luhn_verified(card_number), actual)

class TestIsValid(unittest.TestCase):
    def testValidCardNumber(self):
        card_number = 30536723505217
        self.assertTrue(utils.is_valid(card_number))
    def testInvalidCardNumber(self):
        card_number = '305367235--05217'
        self.assertFalse(utils.is_valid(card_number))

if __name__ == '__main__':
    unittest.main()
