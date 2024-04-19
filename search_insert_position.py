# not the fastest code but i made it myself. i'm happy with it.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        insert = 0

        for i in range(len(nums)):
            if target <= nums[i]:
                break
            else:
                insert +=1
        return insert