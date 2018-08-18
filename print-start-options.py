# Print options for starting a game of Bastille Battalion

# Key: [MA, CA, PA, MD, CD, PD]
barbicanOptions = {
      'Barbarian Barbecue': [2, 0, 0, 2, 0, 0],
      'Babar': [0, 2, 0, 0, 2, 0],
      'Barbershop': [0, 0, 2, 0, 0, 2]
}

drawbridgeOptions = {
    'Draftsman': [0, 0, 0, 2, 2, 2],
    'Art Nouveau': [0, 0, 2, 0, 0, 1],
    'Brutalist': [1, 1, 1, 0, 0, 0]
}

moatOptions = {
    'Sharks': [0, 0, 1, 1, 0, 0],
    'Lava': [1, 0, 0, 0, 1, 0],
    'Truth Serum': [0, 1, 0, 0, 0, 1]
}

murderHoleOptions = {
    'Gesture': [0, 0, 1, 0, 0, 0],
    'Cannon': [1, 0, 0, 0, 0, 0],
    'Catapult': [0, 1, 0, 0, 0, 0]
}

optionCombinations = {}

for barbicanOption in barbicanOptions:
    for drawbridgeOption in drawbridgeOptions:
        for murderHoleOption in murderHoleOptions:
            for moatOption in moatOptions:
                # Calculate summed stats for this combination
                stats = [0, 0, 0, 0, 0, 0]
                for x in range(6):
                    stats[x] = barbicanOptions[barbicanOption][x] + drawbridgeOptions[drawbridgeOption][x] \
                               + murderHoleOptions[murderHoleOption][x] + moatOptions[moatOption][x]

                optionCombinations[barbicanOption + ", " + drawbridgeOption + ", " + murderHoleOption + ", " + moatOption] = stats


def print_all_combinations():
    for optionCombination in optionCombinations:
        print(optionCombination)
        stats = optionCombinations[optionCombination]

        statsSum = sum(stats)
        print("Stats:" + str(stats) + " sum: " + str(statsSum))
        print()

# print_all_combinations()

def print_combinations_with_highest_stats_sum():
    for optionCombination in optionCombinations:
        stats = optionCombinations[optionCombination]
        statsSum = sum(stats)
        if statsSum == 13:
            print(optionCombination)
            print("Stats:" + str(stats) + " sum: " + str(statsSum))
            print()

print_combinations_with_highest_stats_sum()