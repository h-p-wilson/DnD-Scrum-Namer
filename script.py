#!/usr/bin/env python3
# This is so stupid but it helped kill an hour
import json
import random
import textwrap
from pick import pick


class SpellClass:
    bard = 'Bard'
    cleric = 'Cleric'
    druid = 'Druid'
    paladin = 'Paladin'
    ranger = 'Ranger'
    sorcerer = 'Sorcerer'
    warlock = 'Warlock'
    wizard = 'Wizard'


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Input: class name
# Process: Filter json by class (user input)
# Select random spell from new list
# Output: spell name
def choose_spell(class_name):
    # Load the data from the local spells.json file
    with open('spells.json') as f:
        data = json.load(f)
        # Filter the data by class
        filteredData = [spell for spell in data if class_name in spell['class']]
        # Select random spell
        randomSpell = filteredData[random.randint(0, len(filteredData) - 1)]
        # Splits spell description into a list
        chosenSpellList = randomSpell['desc'].split(".")
        # Takes first two elements (first two sentences) and adds them to string
        chosenSpellString = (chosenSpellList[0]) + ". " + chosenSpellList[1] + "."
        # Removing every instance of <p> and </p> from the spell description
        chosenSpellString = chosenSpellString.replace("<p>", "")
        chosenSpellString = chosenSpellString.replace("</p>", "")
        return Color.GREEN + randomSpell['name'] + Color.END + "\n" + textwrap.fill(chosenSpellString, width=100)

        # Print out list of all SpellClass variables
        # Then take user input for class
        # Return class name


def choose_class():
    options = ["Bard - An inspiring magician", "Cleric - A priestly champion", "Druid - A priest of the Old Faith",
               "Paladin - A holy warrior", "Ranger - A warrior", "Sorcerer - A spellcaster",
               "Warlock - A wielder of magic", "Wizard - A scholarly magic-user"]
    title = "Choose a class: "
    option, index = pick(options, title)
    optionString = option.split(" ")[0]
    class_name = optionString
    print(Color.BOLD + "\nYou chose " + class_name + Color.END)
    # Return class name
    return class_name


if __name__ == '__main__':
    # Title
    print()
    title = Color.BOLD + "SOARCERER'S SPELLBOOK" + Color.END
    sparkle = Color.GREEN + "+" + Color.END + Color.RED + "=" + Color.END
    print(sparkle * int(len(title) / 2))
    print((" " * int(len(title) / 8)) + title)
    print(sparkle * int(len(title) / 2))
    status = True
    print()

    begin = input(
        Color.BOLD + Color.RED + "HIT ENTER TO BEGIN" + Color.END)
    # Main Loop
    while status is True:
        # Print random entry
        print('\n' + Color.BOLD + choose_spell(choose_class()) + Color.END + '\n')
        # Continue loop or break
        v = input(
            Color.BOLD + "Choose Another?" + Color.END + " [" + Color.GREEN + 'y' + Color.END + '/' + Color.RED + 'n' + Color.END + ']' + "\n").lower()
        print()
        if v == 'n':
            print(Color.RED + Color.BOLD + "May the sprint begin!" + Color.END)
            break
        if v == 'y':
            continue
