# -*- coding: utf-8 -*-

import copy

TEST = False

# Read input data
with open("day-8/input.txt", "r") as f:
    instructions = f.read().split("\n")

if TEST:
    with open("day-8/test.txt", "r") as f:
        instructions = f.read().split("\n")

instructions = [[instruction.split(" ")[0], int(instruction.split(" ")[1])] for instruction in instructions]


class GameConsole:
    def __init__(self):
        self.intcode_position = 0
        self.accumulator = 0
        self.walk = []

    def acc(self, value):
        self.accumulator += value
        self.intcode_position += 1

    def jmp(self, value):
        self.intcode_position += value

    def nop(self):
        self.intcode_position += 1

    def debug_instructions(self, instructions):
        # Check if position hasn't already been reached while still being in the instruction list
        while (self.intcode_position not in self.walk) and (self.intcode_position < len(instructions)):
            # Add current position to the walk
            self.walk.append(self.intcode_position)
            # Read instruction
            action, value = instructions[self.intcode_position]

            # Execute instruction
            if action == "acc":
                self.acc(value)
            elif action == "jmp":
                self.jmp(value)
            elif action == "nop":
                self.nop()

        self.reached_end = self.intcode_position >= len(instructions)

        return (self.accumulator, self.walk, self.reached_end)

    def read_instructions(self, instructions):
        self.intcode_position = 0
        while 0 <= self.intcode_position < len(instructions):
            action, value = instructions[self.intcode_position]
            if action == "acc":
                self.acc(value)
            elif action == "jmp":
                self.jmp(value)
            elif action == "nop":
                self.nop()

        return (self.accumulator, self.walk)


# Part 1
console = GameConsole()
accumulator, buggy_walk, reached_end = console.debug_instructions(instructions)
print(f"Part 1: last accumulator value before looping is {accumulator}")


# Part 2


def debug(instructions, candidate_positions):
    for position in candidate_positions:
        # Create new console instance
        console = GameConsole()
        # Create new list of instructions
        new_instructions = change_instructions(copy.deepcopy(instructions), position)
        # Debug
        accumulator, walk, reached_end = console.debug_instructions(new_instructions)

        if reached_end:
            return console


def change_instructions(instructions, position):
    instruction = instructions[position]
    action, value = instruction

    # Update action at given position
    if action == "jmp":
        instructions[position][0] = "nop"
    else:
        instructions[position][0] = "jmp"

    return instructions


candidate_positions = [position for position in buggy_walk if instructions[position][0] in ["jmp", "nop"]]
degugged_console = debug(instructions, candidate_positions)

print(f"Part 2: debugged accumulator value after program terminates is {degugged_console.accumulator}")
