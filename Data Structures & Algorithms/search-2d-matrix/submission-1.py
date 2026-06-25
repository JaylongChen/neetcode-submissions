class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                l, r = 0, len(row) - 1
                while l <= r:
                    index = (l + r) // 2
                    if target == row[index]:
                        return True
                    elif target > row[index]:
                        l = index + 1
                    elif target < row[index]:
                        r = index - 1
                    else: 
                        return False
            else:
                continue
        return False