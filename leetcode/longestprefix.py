class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        current_prefix = strs[0]
        for string in strs[1:]:
            while string.find(current_prefix) != 0:
                current_prefix = current_prefix[:-1]
                if not current_prefix:
                    return ""
        return current_prefix
        
resolve = Solution()
print(resolve.longestCommonPrefix(["flower","flow","flight"]))