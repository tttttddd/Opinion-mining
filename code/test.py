
def sortedSquares(nums: [int]) -> [int]:
    fushu = []
    i = 0
    if len(nums) == 0:
        return fushu
    while  i < len(nums) and nums[i] < 0:
        fushu.append(nums[i]*nums[i])
        i = i + 1
    res = []
    j = i - 1
    while (i < len(nums)) and (j >= 0):
        print(1)
        if nums[i]*nums[i] < fushu[j]:
            res.append(nums[i]*nums[i])
            i = i + 1
        else:
            res.append(fushu[j])
            j = j - 1
    if j < 0:
        while i < len(nums):
            res.append(nums[i]*nums[i])
            i = i + 1
    else:
        while j >= 0:
            res.append(fushu[j])
            j = j - 1
    return res


if __name__ == "__main__":

    print(sortedSquares([-4,-1,0,2,5]))