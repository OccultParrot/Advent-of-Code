"""
Advent of Code Day 1

Little notes of important stuff from the riddle I jotted down while reading:

0 - 99

the document contains a sequence of rotations formatted following this pattern:
L4

L or R (which way it turns) then the distance of how far to turn it

L = -1
R = 1

distance is equal to Direction * distance

If the dial was pointing at 11, R8 would cause the dial to point at 19. then L19 would cause the dial to point at 0.

Turning the dial is circular, so if it goes past 99, it wraps around to 0. If it goes below 0, it wraps around to 99.

Dial at 5, L10 -> 95, R5 -> 0

Dial **STARTS** at 50

The password is how many times the dial is left pointing at 0 after any rotation.



"""

with open("input.txt", "r") as f:
    # Cleaning up the data
    data = [line.strip() for line in f.readlines()]
    dial_position = 50
    zero_landings = 0
    zero_passes = 0

    for line in data:
        # L moves back (-1) and R moves forward (1)
        direction = -1 if line[0] == "L" else 1
        distance = int(line[1:])
        offset = direction * distance

        # For puzzle one, we count how many times we *pass* zero
        for i in range(distance):
            if (dial_position + i * direction) % 100 == 0:
                zero_passes += 1

        # For puzzle two, we count how many times we *land on* zero
        dial_position = (dial_position + offset) % 100
        if dial_position == 0:
            zero_landings += 1

    print(f"Answer to puzzle 1: {zero_landings}")
    print(f"Answer to puzzle 2: {zero_passes}")
