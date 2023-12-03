#Regex library:
import re

# -- Methods --

# Returns the first integer in a string via regex check
def extract_int(input_string:str):
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

power_total = 0

for line in file:
    # To start with, we have no cubes. The minimum possible are 0...
    red_min, green_min, blue_min = 0, 0, 0

    # Only care about the game details now, ID irrelevant.
    game = line.split(':')[1].strip('\n')

    # Split each game into its rounds
    game_rounds = game.split(';')

    for round in game_rounds:
        RGB_counts = check_colours(round)

        # I hate this so much but I'm too tired to do better
        if RGB_counts[0] > red_min:
            red_min = RGB_counts[0]
        if RGB_counts[1] > green_min:
            green_min = RGB_counts[1]
        if RGB_counts[2] > blue_min:
            blue_min = RGB_counts[2]

    ''' Not sure if there being an unknown (min 0) number 
    should count as power=0, or if min should be set to 1 ... '''
    
    # Get the 'power score' of this game:
    power_total += (red_min * green_min * blue_min)

print("The sum of the 'power' of these game sets is: {}".format(power_total))