# -*- coding: utf-8 -*-

# Read input data
with open("day_5/input.txt", "r") as f:
    boarding_passes = f.read().split("\n")


def read_binary(encoding, zero_flag, one_flag):
    value = 0
    for i in range(1, len(encoding) + 1):
        value += int(encoding[-i].replace(zero_flag, "0").replace(one_flag, "1")) * (2 ** (i - 1))
    return value


def get_seat_id(seat, row_zero_flag, row_one_flag, col_zero_flag, col_one_flag, row_encoding_length):
    row_part = seat[:row_encoding_length]
    col_part = seat[(-len(seat) + row_encoding_length) :]
    seat_id = read_binary(row_part, row_zero_flag, row_one_flag) * 8 + read_binary(
        col_part, col_zero_flag, col_one_flag
    )
    return seat_id


# Part 1
max_id = 0
seat_ids = [get_seat_id(boarding_pass, "F", "B", "L", "R", 7) for boarding_pass in boarding_passes]
max_id = max(seat_ids)

print(f"Part 1: maximum ID encountered is {max_id}")

# Part 2
seat_ids = sorted(seat_ids)
for i, seat in enumerate(seat_ids[1:]):
    if seat != seat_ids[i] + 1:
        seat_id = seat - 1
        break

print(f"Part 2: seat ID found is {seat_id}")
