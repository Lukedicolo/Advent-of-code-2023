#Regex library:
import re

# -- Methods --
# Returns the first integer in a string via regex check
def extract_int(input_string):
    try:
        return int(re.findall(r'\d+', input_string)[0])
    except:
        return 0

# Checks if a string contains 'red', 'green' or 'blue', then extracts an integer if match.
def check_colours(round_details:str):
    red_count, green_count, blue_count = 0, 0, 0

    colour_sections = round_details.split(',')
    for section in colour_sections:
        if 'red' in section:
            red_count = extract_int(section)
        elif 'green' in section:
            green_count = extract_int(section)
        elif 'blue' in section:
            blue_count = extract_int(section)

    return [red_count, green_count, blue_count]

# -- Script starts here --
file = open('input.txt', 'r').readlines()

# Set up counter for the sum of valid game IDs:
ID_total = 0

# Want to check against these max colour values: [max_red, max_green, max_blue]
RGB_max = [12, 13, 14]

for line in file:
    # Assume the Elf isn't a cheating prick
    game_possible = True

    # Break line into prefix and the game rounds
    prefix, game = line.split(':')
    
    # Extract ID from prefix with regex
    game_ID = extract_int(prefix)

    # Split each game into its rounds
    game_rounds = game.strip('\n').split(';')

    for round in game_rounds:
        RGB_counts = check_colours(round)

        # Compare the actual counts to max values
        for count, max in zip(RGB_counts, RGB_max):
            if count > max:
                # Elf is a cheating prick.
                game_possible = False

    # If the game hasn't been ruled out by the checks, add ID to score.
    if game_possible:
        ID_total += game_ID

print('The sum of valid game IDs is: {}'.format(ID_total))