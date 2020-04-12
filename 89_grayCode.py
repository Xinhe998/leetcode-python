class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * pow(2, n)

        for i in range(1, n+1):
            pointer = (pow(2, i) / 2) - 1
            for j in range(pointer+1, pow(2, i)):
                result[j] = pow(2, i-1) + result[pointer]
                pointer -= 1
        return result


solution = Solution()
print solution.grayCode(0)
