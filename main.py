from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    #YOUR ANSWER
    AnswerList = []
    
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                AnswerList.append(i)
                AnswerList.append(j)
                
    return AnswerList
