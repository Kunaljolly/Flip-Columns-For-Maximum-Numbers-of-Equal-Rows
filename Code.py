from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ma = 0
        for x in range(m):
            ns = 0 
            ni = 0  
            flipped_row = [1 - val for val in matrix[x]]

            for y in range(m):
                if matrix[y] == matrix[x]:
                    ns += 1  
                elif matrix[y] == flipped_row:
                    ni += 1  
            ma = max(ma, ns + ni)
        return ma
