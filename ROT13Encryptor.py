# ROT13 Encryptor
# This program takes text files as input and encrypts them using an ROT13 algorithm
# Programming began circa June 2021
# A program by Tyler Serio
# Python > 3.7

import os
import sys

alphkey = {
    "A": "N",
    "a": "n",
    "B": "O",
    "b": "o",
    "C": "P",
    "c": "p",
    "D": "Q",
    "d": "q",
    "E": "R",
    "e": "r",
    "F": "S",
    "f": "s",
    "G": "T",
    "g": "t",
    "H": "U",
    "h": "u",
    "I": "V",
    "i": "v",
    "J": "W",
    "j": "w",
    "K": "X",
    "k": "x",
    "L": "Y",
    "l": "y",
    "M": "Z",
    "m": "z",
    "N": "A",
    "n": "a",
    "O": "B",
    "o": "b",
    "P": "C",
    "p": "c",
    "Q": "D",
    "q": "d",
    "R": "E",
    "r": "e",
    "S": "F",
    "s": "f",
    "T": "G",
    "t": "g",
    "U": "H",
    "u": "h",
    "V": "I",
    "v": "i",
    "W": "J",
    "w": "j",
    "X": "K",
    "x": "k",
    "Y": "L",
    "y": "l",
    "Z": "M",
    "z": "m",
    }

def main_menu():
    selecting = 1
    print("Welcome to the ROT13 Encryptor!")
    while selecting == 1:
            # Display the options menu
            print("What would you like to do? Options:")
            print("")
            print("Encrypt - [e]")
            print("Decrypt - [d]")
            print("Exit - [0]")
            print("")
            selection = input("Please make a selection: ")

            # It's easier to program the illusion of choice then it is
            # to explain why the algorithm is identical either way
            if selection == "e":
                    print("You have chosen [e] - encrypt")
                    print("")
                    encrypt = 1
                    file = file_selection()
                    ROT13(file, encrypt)

            # It's easier to program the illusion of choice then it is
            # to explain why the algorithm is identical either way
            if selection == "d":
                    print("You have chosen [d] - decrypt")
                    print("")
                    encrypt = 0
                    file = file_selection()
                    ROT13(file, encrypt)
            
            # Exit if selected
            if selection == "0":
                    exit()

            if selection != "e" and selection != "d" and selection != "0":
                    print("You have chosen " + str(selection) + ". That is not a proper selection.")
                    print("")

def file_selection():
    # Display files that can be encrypted/decrypted
    file_list = []
    selection_list = []
    os.chdir("input/")
    cwd = os.getcwd()
    for file in os.listdir(str(cwd)):
        file_list.append(file)
    selection_list.extend(range(1, (len(file_list) + 1)))
    os.chdir("..")
    display_file_selection = True
    while display_file_selection == True:
        place = -1
        printing = 1
        print("Which file  would you like to choose?")
        print("If you would like to exit, press [0].")
        print("The available files are listed below:")
        print("")
        while printing == 1:
            place += 1
            if place >= len(selection_list):
                  printing = 0
                  print("")
                  print("[0] - Exit")
                  print("")
                  break
            print("[" + str(selection_list[place]) + "] - " + str(file_list[place]))

        print("Which file would you like to use?")
        file_selection = input("Please choose one from the list: ")
        if file_selection == "0":
            exit()
        try:
            file_list[int(file_selection) - 1]
            print("You have chosen: [" + str(file_selection) + "] - " + str(file_list[int(file_selection) - 1]))
            print("Done!")
            print("")
            return file_list[int(file_selection) - 1]
            exit()
            
        except IndexError:
            print("You have chosen: [" + str(file_selection) + "]")
            print("That is not a proper selection!")
            print("")

        

        # Exit the program
        if file_selection == "0":
            exit()         

def ROT13(file, encrypt):
    # Run the encryption algorithm
    if encrypt == 1:
        outputfile = open("output/" + file.replace(".txt", "_encrypted.txt"), "w")
    if encrypt == 0:
        outputfile = open("output/" + file.replace(".txt", "_decrypted.txt"), "w")
    file = open("input/" + file, "r")
    for line in file:
        characters = split(str(line))
        stepping = 1
        step = 0
        while stepping == 1:
            if characters[step] in alphkey:
                outputfile.write(alphkey[characters[step]])
            else:
                outputfile.write(characters[step])
            step += 1
            if step >= len(characters):
                stepping = 0
    file.close()
    outputfile.close()

def split(word):
    return[char for char in word]

main_menu()
        
