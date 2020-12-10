# -*- coding: utf-8 -*-

# Load necessary modules
import collections


TEST = False
INPUT_JOLTAGE = 0


# Read input data
with open("day_10/input.txt", "r") as f:
    joltages = [int(x) for x in f.read().split("\n")]

if TEST:
    # Override input data
    with open("day_10/test.txt", "r") as f:
        joltages = [int(x) for x in f.read().split("\n")]


# Part 1
sorted_joltages = sorted(joltages)
output_joltage = sorted_joltages[-1] + 3
# Add charging outlet and built-in adaptor joltages to form the whole joltage sequence
sorted_joltages = [INPUT_JOLTAGE] + sorted_joltages + [output_joltage]

# Compute and count diffs
joltage_diffs = [joltage - sorted_joltages[i - 1] for i, joltage in enumerate(sorted_joltages) if i > 0]
diff_counter = collections.Counter(joltage_diffs)

print(f"Part 1: product found is {diff_counter.get(1) * diff_counter.get(3)}")


# Part 2


def split_list(list_to_split, split_value):
    size = len(list_to_split)
    idx_list = [idx + 1 for idx, val in enumerate(list_to_split) if val == split_value]
    res = [list_to_split[i:j] for i, j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))]
    return res


def count_distinct_ways(diff_list):
    arrangement_counter = 0
    if len(diff_list) == 1:
        return 1

    for i in range(min(3, len(diff_list) - 1)):
        if diff_list[i] == 3:
            arrangement_counter = count_distinct_ways(diff_list[i + 1 :])
        else:
            arrangement_counter += count_distinct_ways(diff_list[i + 1 :])

    return arrangement_counter


# Split joltage difference list on 3 to have sublists of consecutive joltage adapters
split_joltage_diffs = split_list(joltage_diffs, 3)

# Count arrangements for each sublist
arrangement_counter = 1
for sublist in split_joltage_diffs:
    arrangement_counter *= count_distinct_ways(sublist)

print(f"Part 2: number of distinct arrangements found is {arrangement_counter}")
