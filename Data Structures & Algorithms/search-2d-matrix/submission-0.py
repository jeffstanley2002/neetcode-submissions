class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rw=-1
        for i in range(1,len(matrix)):
            if matrix[i-1][0] <= target < matrix[i][0]:
                rw=i-1
                break
        lis=matrix[rw]

        def binary_search(lis,t):
            l,r=0,len(lis)-1
            while l<=r:
                mid=(r+l)//2
                if lis[mid]==t:
                    return True
                elif t>lis[mid]:
                    l=mid+1
                else:
                    r=mid-1
            return False
        return (binary_search(lis,target))
        