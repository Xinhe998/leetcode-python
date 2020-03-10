class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if stack and map[stack[-1]] == i:
                del stack[-1]
            else:
                if i not in map:
                    return False
                stack.append(i)
        if not stack:
            return True


solution = Solution()
print solution.isValid('{[()]}')
