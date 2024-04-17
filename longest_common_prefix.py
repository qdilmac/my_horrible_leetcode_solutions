class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # solution = ""

        prefix = strs[0]
        prefix_len = len(prefix)

        for i in strs[1:]: #we start form 2. index because we already took the first one as a prefix to iterate from
            while prefix != i[0:prefix_len]:
                prefix_len -= 1
                if prefix_len == 0:
                    return ""
                prefix = prefix[0:prefix_len]
        return prefix
