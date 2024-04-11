from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  # YOUR ANSWER
  ans = []
  plag=0
  for i in range(len(nums)):
    for j in range(i+1,len(nums),1):
      if (nums[i]+nums[j]) == target:
        ans.append(i)
        ans.append(j)
        plag=1
        break
    if plag==1:
      break

  return ans