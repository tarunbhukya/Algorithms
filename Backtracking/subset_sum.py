"""
Subset sum problem is to find subset of elements that are selected from a given set
whose sum adds up to a given number K. We are considering the set contains non-negative values.
It is assumed that the input set is unique (no duplicates are presented).

Trick: Solve it in terms of printing all paths in a set and with a blocker
"""

def print_solution(select_set, num):
    for i in range(len(num)):
        if select_set[i] == 1:
            print(num[i], end=" ")
    print(" is 35")
    print()

def subset_util(num, target_sum, select_set, index, total_sum):
    if total_sum == target_sum:
        print_solution(select_set, num)
        return

    if index == len(num) - 1:
        return

    if total_sum < target_sum:
        # if index is selected
        new_subset = [] + select_set
        new_subset[index] = 1
        subset_util(num, target_sum, new_subset, index + 1, total_sum + num[index])

        # if index is not selected
        subset_util(num, target_sum, select_set, index + 1, total_sum)
        return

    else:
        return


def solve_subset(num, target_sum):
    # select set would act as wether a number is selected from a set or not
    select_set = [0 for i in range(len(num_set))]
    subset_util(num, target_sum, select_set, 0, 0)


num_set = [10, 7, 5, 18, 12, 20, 15]
solve_subset(num_set, 35)