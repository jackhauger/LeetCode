class Solution2:
    def romanToInt(self, s: str) -> int:
        stack = []
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0

        total = 0
        prevValue = 0

        for char in reversed(s):
            currValue = dict[char]

            if currValue < prevValue:
                total -= currValue
            else:
                total += currValue

            prevValue = currValue

        return total

solution = Solution2()

z = solution.romanToInt('MCDLXXVI')
print(z)


