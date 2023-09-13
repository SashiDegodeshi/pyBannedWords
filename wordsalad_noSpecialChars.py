## ================================================================================== ##
## Banned word variation generator | Written by: Joshua Alto on 9/12/2023 at 11:23 PM ##
## ================================================================================== ##
## This generator will read a list of input words from input_words.txt and use like   ##
## characters to create variations of those words. I wrote this program to create     ##
## word lists for an old phpbb forum software banned word filter but it can be used   ##
## for anything I suppose. It outputs in to a wordlist folder where each word has its ##
## own text file with the original word and its variations.                           ##
## ================================================================================== ##
## Feel free to use this or modify it to suit your needs, just give me credit for my  ##
## source code.                                                                       ##
## ================================================================================== ##

import re
import itertools
import os

# Here we define what symbols look similar to our letters and numbers
def generate_variations(word):
    symbol_sets = {
        'a': ['a', '4', 'A'],
        'b': ['b', 'B', '8'],
        'c': ['c', 'C'],
        'd': ['d', 'D'],
        'e': ['e', '3', 'E'],
        'f': ['f', 'F'],
        'g': ['g', 'G', '6', '9'],
        'h': ['h', 'H'],
        'i': ['i', '1', 'I'],
        'j': ['j', 'J'],
        'k': ['k', 'K'],
        'l': ['l', 'L', '1'],
        'm': ['m', 'M'],
        'n': ['n', 'N'],
        'o': ['o', '0', 'O'],
        'p': ['p', 'P'],
        'q': ['q', 'Q'],
        'r': ['r', 'R'],
        's': ['s', '5', 'S'],
        't': ['t', 'T', '7'],
        'u': ['u', 'U', 'v', 'V'],
        'v': ['v', 'V', 'U', 'u'],
        'w': ['w', 'W', 'vv', 'VV'],
        'x': ['x', 'X'],
        'y': ['y', 'Y'],
        'z': ['z', 'Z', '2'],
        '0': ['0', 'o', 'O'],
        '1': ['1', 'i', 'I' , 'l'],
        '3': ['3', 'e', 'E'],
        '5': ['5', 's', 'S'],
        '7': ['7', 't', 'T'],
        '8': ['8', 'b', 'B'],
        '9': ['9', 'g', 'G'],
    }

    # Our word variation generator
    def generate_variations_recursive(word, current_variation, index):
        if index == len(word):
            variations.add(''.join(current_variation))
            return

        char = word[index]
        if char in symbol_sets:
            for symbol in symbol_sets[char]:
                current_variation[index] = symbol
                generate_variations_recursive(word, current_variation, index + 1)
        else:
            current_variation[index] = char
            generate_variations_recursive(word, current_variation, index + 1)

    variations = set()
    current_variation = list(word)
    generate_variations_recursive(word, current_variation, 0)

    return variations

if __name__ == "__main__":
    # Read words from the text file
    with open("input_words.txt", "r") as word_file:
        words = [line.strip() for line in word_file.readlines()]

    output_directory = "noSCwordlists"  # Directory to save the files

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for word in words:
        variations = generate_variations(word)
        variations = list(variations)  # Convert set to a list to remove duplicates

        # Write variations to a text file in the specified directory
        print(f"Processing {word}")
        output_file_path = os.path.join(output_directory, f"{word}.txt")
        with open(output_file_path, "w") as file:
            file.write(f"{word}" + "\n")
            for variation in variations:
                file.write(variation + "\n")
    print("Generation Complete")
