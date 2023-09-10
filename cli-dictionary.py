"""
Command-Line Dictionary

This script offers a command-line interface where users can input a word and get its definition.
"""

import json
import difflib

data = json.load(open("data.json"))

def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        closest_match = difflib.get_close_matches(word, data.keys())[0]
        confirm = input(f"Did you mean '{closest_match}'? Enter Y for yes or N for no: ")
        if confirm.lower() == 'y':
            return data[closest_match]
        else:
            return "The word doesn't exist. Please double-check it."
    else:
        return "The word doesn't exist. Please double-check it."

word_input = input("Enter a word: ")
print(get_definition(word_input))
