class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        index = 1
        carry = 0
        result = []
        if len(a) > len(b):
            b = '0' * (len(a)-len(b)) + b
        else:
            a = '0' * (len(b)-len(a)) + a
        while index <= max(len(a), len(b)) or carry != 0:
            if index <= len(a) and index <= len(b):
                if int(a[-index]) + int(b[-index]) + carry < 2:
                    result.append(int(a[-index]) + int(b[-index]) + carry)
                    carry = 0
                elif int(a[-index]) + int(b[-index]) + carry == 2:
                    result.append(0)
                    carry = 1
                else:
                    result.append(1)
                index += 1
            else:
                result.append(1)
                carry = 0
        return str(result[::-1]).strip('[]').replace(', ','')


solution = Solution()
print solution.addBinary('11', '1')
