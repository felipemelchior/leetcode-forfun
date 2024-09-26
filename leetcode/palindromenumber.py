# https://leetcode.com/problems/palindrome-number/class Solution:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False

resolve = Solution()
print(resolve.isPalindrome(121))