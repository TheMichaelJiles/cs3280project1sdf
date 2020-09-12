#! /usr/bin/python
import utils
import sys

def main():
    pad_length = 25
    card_types_path = sys.argv[1]
    card_types = load_card_types(card_types_path)
    card_number = input("Please enter a credit card number:")
    if (not utils.is_valid(card_number)):
        print(pad_spaces_to_length("Credit card number: ",pad_length) + "Invalid")
        print(pad_spaces_to_length("Credit card type: ",pad_length) + "Invalid")
        print(pad_spaces_to_length("Luhn Verification: ",pad_length) + "N/A")
    else:
        print(pad_spaces_to_length("Credit card number: ",pad_length) + card_number)
        name = get_card_type(card_types, card_number)
        print(pad_spaces_to_length("Credit card type: ",pad_length) + str(name))
        print(pad_spaces_to_length("Luhn Verification: ",pad_length) + utils.luhn_verified(card_number))

def pad_spaces_to_length(string, length):
    string_length = len(string)
    for number in range(len(string),length):
        string += " "
    return string

def get_card_type(card_types, card_number):
    for type in card_types:
        name = type[0]
        lengths = type[1]
        for length in lengths:
            if length == len(card_number):
                prefixes = type[2]
                for prefix in prefixes:
                    prefix_length = len(str(prefix))
                    if int(card_number[0:prefix_length]) == int(prefix):
                        return name
    return "Invalid"


def load_card_types(filepath):
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
        card_type_tuple = (line[0])
        for length in lengths:
            length_list.append(int(length))
        for prefix in prefixes:
            if('-' in prefix):
                prefix_split = prefix.split('-')
                start = int(prefix_split[0])
                end = int(prefix_split[1])
                prefix_range = list(range(start, end))
                for number in prefix_range:
                    prefix_list.append(number)
            else:
                prefix_list.append(int(prefix))
        card_tuple = (line[0], length_list, prefix_list)
        card_types.append(card_tuple)
    return card_types

main()
