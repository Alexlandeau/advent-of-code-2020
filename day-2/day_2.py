# -*- coding: utf-8 -*-

# Load necessary modules
import re

# Read input data
with open("day-2/input.txt", "r") as f:
    data = f.read().split("\n")

PARSER_PATTERN = "(\d+)-(\d+)\s([a-z]):\s(.*)"


def check_password_validity_pt1(password, letter, minimum, maximum):
    return minimum <= password.count(letter) <= maximum


def check_password_validity_pt2(password, letter, minimum, maximum):
    check_1 = password[minimum - 1] == letter
    check_2 = password[maximum - 1] == letter
    return check_1 + check_2 == 1


valid_passwords_count_pt1 = 0
valid_passwords_count_pt2 = 0

for line in data:
    minimum, maximum, letter, password = re.search(PARSER_PATTERN, line).groups()
    minimum = int(minimum)
    maximum = int(maximum)

    if check_password_validity_pt1(password, letter, minimum, maximum):
        valid_passwords_count_pt1 += 1
    if check_password_validity_pt2(password, letter, minimum, maximum):
        valid_passwords_count_pt2 += 1

print(f"Part 1: Found {valid_passwords_count_pt1} valid passwords")
print(f"Part 2: Found {valid_passwords_count_pt2} valid passwords")
