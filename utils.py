'''
Utils that are used for validating credit card numbers
author: Michael Jiles
Version: 1.0
'''
import re

def luhn_verified(credit_card_number):
    '''
    Returns 'Authentic' if credit_card_number is real, or 'Fake' if it is not.
    '''

    if not is_valid(credit_card_number):
        return 'N/A'

    number_list = [int(i) for i in str(credit_card_number)]
    last_digit = number_list.pop()

    number_list.reverse()
    length = len(number_list)

    for i in range(length):
        if (i % 2) == 0:
            number = number_list[i]
            number = number * 2
            if number > 9:
                number = number - 9
            number_list[i] = number
    curr_sum = 0

    for number in number_list:
        curr_sum = curr_sum + number

    if (curr_sum % 10) != 10 - last_digit:
        return 'Fake'

    return 'Authentic'


def is_valid(sequence):
    '''
    Returns true if the specified string sequence is a valid credit card number,
    and false otherwise.
    '''
    regex = r'(\d{13}\d{0,6})|(\d{4}(\-\d{4}){3})|(\d{4}(\s\d{4}){3})'
    return re.match(regex, str(sequence))
