# -*- coding: utf-8 -*-

# Load necessary modules
import sys
from pathlib import Path


# Add parent folder to python path and import function from day 1 solution
sys.path.append(str(Path(".").absolute()))
from day_1.day_1 import get_sum_terms


TEST = False
DEFAULT_PREAMBLE_LENGTH = 25


# Read input data
with open("day_9/input.txt", "r") as f:
    outputs = [int(x) for x in f.read().split("\n")]

if TEST:
    # Override constants
    DEFAULT_PREAMBLE_LENGTH = 5
    # Override input data
    with open("day_9/test.txt", "r") as f:
        outputs = [int(x) for x in f.read().split("\n")]


def find_invalid_output(outputs, preamble_length=DEFAULT_PREAMBLE_LENGTH):
    assert len(outputs) > preamble_length, "output list is shorter than preamble"

    for i, reference_value in enumerate(outputs[preamble_length:]):
        if get_sum_terms(outputs[i : preamble_length + i], 2, reference_value) == []:
            return i, reference_value


# Part 1
first_invalid_index, first_invalid_value = find_invalid_output(outputs)
print(f"Part 1: first invalid value found is {first_invalid_value}")

# Part 2
for end in range(1, first_invalid_index):
    for start in range(0, end):
        if sum(outputs[start:end]) == first_invalid_value:
            contiguous_set = outputs[start:end]
            break

print(f"Part 2: encryption weakness is {min(contiguous_set) + max(contiguous_set)}")
