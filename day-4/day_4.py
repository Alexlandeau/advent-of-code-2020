# -*- coding: utf-8 -*-

# Load necessary modules
import re

# Read input data
with open("day-4/input.txt", "r") as f:
    passports = f.read().split("\n\n")


def parse_passports(passports):
    passports = [" ".join(passport.split("\n")) for passport in passports]
    passports = [passport.split() for passport in passports]
    return passports


def passport_to_dict(passport):
    return dict([attribute.split(":") for attribute in passport])


def check_passport_keys(passport):
    test = all(x in passport.keys() for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    return test


def check_passport_values(passport):
    # Check patter validity first
    if all(
        [
            bool(re.match("^\d{4}$", passport.get("byr", "_"))),
            bool(re.match("^\d{4}$", passport.get("iyr", "_"))),
            bool(re.match("^\d{4}$", passport.get("eyr", "_"))),
            bool(re.match("^\d*(cm|in)$", passport.get("hgt", "_"))),
            bool(re.match("^#[a-f0-9]{6}$", passport.get("hcl", "_"))),
            bool(re.match("^amb|blu|brn|gry|grn|hzl|oth$", passport.get("ecl", "_"))),
            bool(re.match("^\d{9}$", passport.get("pid", "_"))),
        ]
    ):
        return all(
            [
                1920 <= int(passport.get("byr")) <= 2002,
                2010 <= int(passport.get("iyr")) <= 2020,
                2020 <= int(passport.get("eyr")) <= 2030,
                ((passport.get("hgt")[-2:] == "in") and (59 <= int(passport.get("hgt")[:-2]) <= 76))
                or ((passport.get("hgt")[-2:] == "cm") and (150 <= int(passport.get("hgt")[:-2]) <= 193)),
            ]
        )
    else:
        return False


passports = parse_passports(passports)
passports = [passport_to_dict(passport) for passport in passports]

# Part 1
passports_validities = [check_passport_keys(passport) for passport in passports]
print(f"Part 1: encountered {sum(passports_validities)} valid passports")

# Part 2
passports_validities = [check_passport_keys(passport) and check_passport_values(passport) for passport in passports]
print(f"Part 2: encountered {sum(passports_validities)} valid passports")
