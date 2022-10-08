from typing import List, Optional


#def two_sum(nums: List[int], target: int) -> List[Optional[int]]:
#    diff_from_target = {}
#    for idx, i in enumerate(nums):
#        if (other_idx := diff_from_target.get(i)) is not None:
#            break
#        diff_from_target[target - i] = idx
#
#    return [other_idx, idx]


def two_sum(nums: List[int], target: int) -> List[Optional[int]]:
    diff_to_idx = {}
    for idx, n in enumerate(nums):
        if n in diff_to_idx:
            return [diff_to_idx[n], idx]
        else:
            diff_to_idx[target - n] = idx


def test_two_sum():
    assert two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum(nums=[3, 2, 4], target=6) == [1, 2]
    assert two_sum(nums=[3, 3], target=6) == [0, 1]
