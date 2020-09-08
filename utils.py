import re

def luhn_verified(credit_card_number):
    '''
    Returns 'Authentic' if credit_card_number is real, or 'Fake' if it is not.
    '''

    if(not is_valid(credit_card_number)):
        return 'N/A'

    number_list = [int(i) for i in str(credit_card_number)]
    print(number_list)
    last_digit = number_list.pop()

    number_list.reverse()

    print(number_list)
    for i in range(len(number_list)):
        if (((i % 2) == 0)):
            number = number_list[i]
            number = number * 2
            if(number > 9):
                number = number - 9
            number_list[i] = number
    sum = 0

    for number in number_list:
        sum = sum + number

    print(number_list)
    print(sum)
    if (sum % 10) != 10 - last_digit:
        return 'Fake'

    return 'Authentic'


def is_valid(sequence):
    '''
    Returns true if the specified string sequence is a valid credit card number,
    and false otherwise.
    '''
    regex = '(\d{13}\d{0,6})|(\d{4}(\-\d{4}){3})|(\d{4}(\s\d{4}){3})'
    return re.match(regex, sequence)
