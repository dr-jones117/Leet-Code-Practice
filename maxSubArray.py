from typing import List

test_list = [[-2,1,-3,4,-1,2,1,-5,4],
              [1],
              [5,4,-1,7,8]]

def maxSubArray(nums: List[int]) -> int:
    maxSub = nums[0]
    curr_sum = 0
    for num in nums:
        if curr_sum < 0:
            curr_sum = 0

        curr_sum += num
        maxSub = max(maxSub, curr_sum)

    return maxSub


def main():
    for idx, test in enumerate(test_list):
        print(f'The maximum of test list {idx} is: {maxSubArray(test)}')

if __name__ == '__main__':
    main()