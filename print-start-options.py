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

murderHoleOptions = {
    'Gesture': [0, 0, 1, 0, 0, 0],
    'Cannon': [1, 0, 0, 0, 0, 0],
    'Catapult': [0, 1, 0, 0, 0, 0]
}

for barbicanOption in barbicanOptions:
    for drawbridgeOption in drawbridgeOptions:
        for murderHoleOption in murderHoleOptions:
            print(barbicanOption + ", " + drawbridgeOption + ", " + murderHoleOption)

            # Calculate and print sum of stats
            sum = [0, 0, 0, 0, 0, 0]
            for x in range(6):
                sum[x] = barbicanOptions[barbicanOption][x] + drawbridgeOptions[drawbridgeOption][x] + murderHoleOptions[murderHoleOption][x]
            print(sum)