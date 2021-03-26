#!/usr/bin/python3
import argparse
import re
from sys import exit


def init_argparse():
    parser = argparse.ArgumentParser()

    #Required arguments
    required = parser.add_argument_group("required arguments")
    required.add_argument("--input", help="input file name", required=True)
    required.add_argument("--min", help="minimum lenght of words", required=True, type=int)
    required.add_argument("--max", help="maximum lenght of words", required=True, type=int)
    required.add_argument("--output", help="output file name", required=True)
    return parser


def read_input_file(file_path: str):
    input_set = set()
    try:
        with open(file_path, 'r', encoding="utf-8") as input_file:
            for line in input_file:
                for word in line.split():
                    input_set.add(word)
    except FileNotFoundError:
        print('Input file not found!\nExiting...')
        exit(1)
    return input_set


def throw_words_charachter(input_set: set):
    input_list = list(input_set)
    selected_word_list = list()

    for word in range(len(input_list)):
        temp_word = input_list[word]
        throw = True
        for char in temp_word:
            if (chr(65) <= char <= chr(90) or chr(97) <= char <= chr(122)):
                throw = False
            else:
                throw = True
                break
        if throw == False:
            selected_word_list.append(input_list[word])
    return selected_word_list


def throw_words_lenght(input_list: list):
    selected_word_list = list()

    #lenght
    for word in range (len(input_list)):
        if args.min <= len(input_list[word]) <= args.max:
            selected_word_list.append(input_list[word])

    return selected_word_list


args = init_argparse().parse_args()


if __name__ == '__main__':
    input_set = read_input_file(args.input)
    selected_word_list0 = throw_words_charachter(input_set)
    selected_word_list = throw_words_lenght(selected_word_list0)
    f_out = open(args.output, 'w')
    for line in range (len(selected_word_list)):
        f_out.write(selected_word_list[line]+"\n")
    f_out.close()






