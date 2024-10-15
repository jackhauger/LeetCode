class Solution:
    def isPalindrome(self, x: int) -> bool:
        space = 0
        other = str(x)
        for i in range(int(len(other) / 2)):
            first = other[space]
            last = other[(len(other) - 1) - space]

            space += 1
            if first != last:
                return False
        return True

solution = Solution()

z = solution.isPalindrome(12421)
print(z)