from typing import List

tests = [
    ([2,7,11,15], 9),
    ([2,3,4], 6),
    ([-1,0], -1)
]

def twoSum(numbers: List[int], target: int) -> List[int]:
    ptr_one, ptr_two = 0, len(numbers) - 1

    while ptr_one < ptr_two:
        sum = numbers[ptr_one] + numbers[ptr_two]
        if sum == target:
            return [ptr_one + 1, ptr_two + 1]
        elif sum > target:
            ptr_two -= 1
        else:
            ptr_one += 1

    return [-1, -1]

def main():
    for test in tests:
        print(f'The indices for target {test[1]} '
              f'are: {twoSum(test[0], test[1])}')

if __name__ == '__main__':
    main()