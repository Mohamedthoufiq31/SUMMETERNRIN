# -*- coding: utf-8 -*-
"""DAY 2 : MINI PROJECT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mdgfk7mk60GHSESsIRgcXyCfW-8cgOTt

MINI PROJECT

1 .Problem statement :
Find all the subsets from a set of numbers whose sum is zero.

Constraint: Subset size must be 5

Set={-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}
"""

from itertools import combinations

def find_zero_sum_subsets(input_set):
    subsets = list(combinations(input_set, 5))
    zero_sum_subsets = [subset for subset in subsets if sum(subset) == 0]
    return zero_sum_subsets

input_set = {-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}
zero_sum_subsets = find_zero_sum_subsets(input_set)

for subset in zero_sum_subsets:
    print(subset)

"""2.Problem statement :
Find all the subsets from a set of numbers whose sum is zero.

Constraint: Subset size must be 3 to 6 only

Set={-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}
"""

from itertools import combinations

def find_zero_sum_subsets(input_set):
    zero_sum_subsets = []
    # Check combinations of size 3, 4, 5, and 6
    for subset_size in range(3, 7):
        subsets = combinations(input_set, subset_size)
        zero_sum_subsets.extend([subset for subset in subsets if sum(subset) == 0])
    return zero_sum_subsets

input_set = {-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}
zero_sum_subsets = find_zero_sum_subsets(input_set)

for subset in zero_sum_subsets:
    print(subset)