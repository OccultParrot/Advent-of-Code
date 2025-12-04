"""
Advent of Code Day 2

Damn kids messed with the computer, smh

now there are invalid ids, which are pairs of numbers?
like 11 and 22, or 432432

The data given is pairs of start IDs and end IDs. I think we increment up from each start and find any that
when cut in half, are the same number as the other half.

Ranges are seperated by ,s and the ids are seperated by -s

11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.

Then add all the invalids together and that's your passcode

Adding up all the invalid IDs in this example produces 1227775554.

Well, lets see how this goes!

=====================
Ok, that worked out pretty well, but now we are in a predicament!
The little twerps decided to also to triplets and octets and such of the ids!

So, 12341234 (1234 two times),
123123123 (123 three times),
1212121212 (12 five times),
and 1111111 (1 seven times) are all invalid IDs.
"""
import time

with open("input.txt", "r") as f:
    start_time = time.time()
    data = [id_range.strip().split("-") for id_range in f.read().split(",")]

    problem_two_solution = 0
    problem_one_solution = 0

    for id_range in data:
        for i in range(int(id_range[0]), int(id_range[1]) + 1):
            id_str = str(i)
            id_len = len(id_str)

            # ====== Problem One ======
            first_half = id_str[:(id_len // 2)] # Getting the FIRST half of the string
            second_half = id_str[(id_len // 2):] # Getting the SECOND half of the string

            if first_half == second_half:
                problem_one_solution += i

            # ====== Problem Two ======
            # Checking for divisions
            for divisor in range(2, id_len + 1):
                # If the length does not divide evenly, skip it
                if id_len % divisor != 0:
                    continue

                chunk_size = id_len // divisor
                splits = [id_str[x:x + chunk_size] for x in range(0, id_len, chunk_size)]

                # Cast to a set to check if there is more than one unique item
                # Sets only contain unique items
                if len(set(splits)) == 1:
                    problem_two_solution += i
                    break

    end_time = time.time()

    total_time = end_time - start_time

    print(f"Solution to problem ONE: {problem_one_solution}")
    print(f"Solution to problem TWO: {problem_two_solution}")
    print(f"Computation Time: {total_time} seconds")
