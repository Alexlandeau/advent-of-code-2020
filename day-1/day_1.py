# -*- coding: utf-8 -*-

# Read input data
with open("day-1/input.txt", "r") as f:
    expenses = f.read().split("\n")
expenses = [int(expense) for expense in expenses]

DEFAULT_SUM_TARGET = 2020


def get_sum_terms(expenses, nb_terms, sum_target=DEFAULT_SUM_TARGET):
    s = set()

    if nb_terms == 2:
        for e1 in expenses:
            e2 = sum_target - e1
            if e2 in expenses:
                s.update([e1, e2])
        return list(s)
    else:
        for i, e1 in enumerate(expenses):
            e2 = sum_target - e1
            new_expenses = [expenses[j] for j in range(len(expenses)) if j != i]
            temp_list = [e1] + get_sum_terms(new_expenses, nb_terms - 1, e2)
            if len(temp_list) == nb_terms:
                print(f"Found matching expenses: {', '.join([str(s) for s in temp_list])}")
                return temp_list


def get_list_product(input_list):
    # Multiply elements one by one
    result = 1
    for x in input_list:
        result = result * x
    return result


# First problem
sum_terms = get_sum_terms(expenses, 2)
product = get_list_product(sum_terms)

if len(sum_terms) == 2:
    print(f"Part 1: Found matching expenses: {', '.join([str(s) for s in sum_terms])}, which product is {product}")
    get_list_product(sum_terms)

# Second problem
sum_terms = get_sum_terms(expenses, 3)
product = get_list_product(sum_terms)

if sum_terms:
    print(f"Part 2: Found matching expenses: {', '.join([str(s) for s in sum_terms])}, which product is {product}")
