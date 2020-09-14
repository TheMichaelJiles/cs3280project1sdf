#! /usr/bin/python
'''
Program that allows validates credit card numbers and identifies what type
of card the number is from.
author: Michael Jiles
Version: 1.0
'''
import sys
sys.path.insert(0, '/home/sjiles1/Documents/SystemsProgrammingProject1')
from src.main.python import utils

def main():
    '''
    The main method that drives the program. Allows user to enter a credit card number,
    and outputs the type as well as if thenumber is authentic.
    '''
    pad_length = 25
    card_types_path = sys.argv[1]
    card_types = load_card_types(card_types_path)
    card_number = input("Please enter a credit card number:")
    if not utils.is_valid(card_number):
        print(pad_spaces_to_length("Credit card number: ", pad_length) + "Invalid")
        print(pad_spaces_to_length("Credit card type: ", pad_length) + "Invalid")
        print(pad_spaces_to_length("Luhn Verification: ", pad_length) + "N/A")
    else:
        print(pad_spaces_to_length("Credit card number: ", pad_length) + card_number)
        name = get_card_type(card_types, card_number)
        print(pad_spaces_to_length("Credit card type: ", pad_length) + str(name))
        print(pad_spaces_to_length("Luhn Verification: ", pad_length) +
              utils.luhn_verified(card_number))

def pad_spaces_to_length(string, length):
    '''
    Takes in a string and a length, pads spaces onto the end
    of the string until the length is reached.
    '''
    for _ in range(len(string), length):
        string += " "
    return string

def get_card_type(card_types, card_number):
    '''
    Returns the card type based on the card_types datastructure
    '''
    for card_type in card_types:
        name = card_type[0]
        lengths = card_type[1]
        for length in lengths:
            if length == len(card_number):
                prefixes = card_type[2]
                for prefix in prefixes:
                    prefix_length = len(str(prefix))
                    if int(card_number[0:prefix_length]) == int(prefix):
                        return name
    return "Invalid"


def load_card_types(filepath):
    '''
    Loads the card_types datastructure
    '''
    file = open(filepath)
    lines = file.readlines()
    card_types = []
    for line in lines:
        line = line.replace(' ', '')
        line = line.split(';')
        lengths = line[1].split(',')
        length_list = []
        prefixes = line[2].split(',')
        prefix_list = []
        for length in lengths:
            length_list.append(int(length))
        for prefix in prefixes:
            if '-' in prefix:
                prefix_split = prefix.split('-')
                prefix_range = list(range(int(prefix_split[0]), int(prefix_split[1])))
                for number in prefix_range:
                    prefix_list.append(number)
            else:
                prefix_list.append(int(prefix))
        card_tuple = (line[0], length_list, prefix_list)
        card_types.append(card_tuple)
    return card_types

if __name__ == '__main__':
    main()
