from typing import List

list_one = [1, 2, 3, 4, 5, 6, 7, 8]
target_one = 4

list_two = [20, 10, 0, 0, 2, 5, 2, 6, 50]
target_two = 70

def twoSum(nums: List[int], target: int) -> List[int]:
    amount_dict = {}
    for idx, num in enumerate(nums):
        amount_dict[num] = idx

    for idx, num in enumerate(nums):
        if (amount_dict.get(target - num) and
                idx != amount_dict.get(target - num)):
            return [idx, amount_dict.get(target - num)]

    return [0, 0]

def main():
    print(twoSum(list_one, target_one))
    print(twoSum(list_two, target_two))

if __name__ == '__main__':
    main()