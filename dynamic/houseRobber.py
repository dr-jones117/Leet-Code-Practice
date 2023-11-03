from typing import List

tests = [
    [1, 2, 3, 1],
    [2, 7, 9, 3, 1]
]


def rob(nums: List[int]) -> int:
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


def main():
    for idx, test in enumerate(tests):
        print(f'Test {idx}\'s max money is {rob(test)}')


if __name__ == '__main__':
    main()
