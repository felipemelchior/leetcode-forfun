#https://leetcode.com/problems/roman-to-integer/
class Solution:

    def romanToInt(self, s: str) -> int:
        answer = 0
        prev = 0
        romanHashMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for char in s[::-1]:
            current = romanHashMap[char] 

            if prev > current:
                answer -= current
            else: 
                answer += current
            prev = current
        return answer

resolve = Solution()  
print(resolve.romanToInt("MCMXCIV"))