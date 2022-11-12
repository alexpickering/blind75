
import heapq

def max_profit(nums):
    min_to_idx_pairs = [(i, nums.index(i)) for i in sorted(nums)]
    max_to_idx_pairs = reversed(min_to_idx_pairs)
    for min_i, min_idx in min_to_idx_pairs:
        for max_i, max_num_idx in max_to_idx_pairs:
            pass


