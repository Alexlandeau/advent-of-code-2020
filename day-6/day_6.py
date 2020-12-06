# -*- coding: utf-8 -*-

# Read input data
with open("day-6/input.txt", "r") as f:
    form_groups = f.read().split("\n\n")


def get_unique_answers(form_group):
    forms = [set(form) for form in form_group.split("\n")]
    return sorted(set(answer for form in forms for answer in form))


def get_common_answers(form_group):
    forms = [set(form) for form in form_group.split("\n")]
    common_answers = set(forms[0].intersection(*forms))
    return sorted(common_answers)


# Part 1
count = 0
for group in form_groups:
    count += len(get_unique_answers(group))

print(f"Part 1: total number of unique answers is {count}")

# Part 2
count = 0
for group in form_groups:
    count += len(get_common_answers(group))

print(f"Part 2: total number of common answers is {count}")
