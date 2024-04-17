"""
First try xd

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(":1,")":2,"{":3,"}":4,"[":5,"]":6}
        
        for i in range(len(s)-1): # -1 to prevent out of bounds error
            if bracket_dict[s[(i+1)]] - bracket_dict[s[i]] != 1 or s[0] == (")","}","]"):      
                return 0
            else:
                return 1
                
Failed at [{}] test case.
"""


"""
Second try

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(":")","{":"}","[":"]"}
        
        for i in range(len(s)-1): # -1 to prevent out of bounds error
            if bracket_dict[s[(i)]] == s[i+1]:
                return 1
            else:
                return 0
                
-> This in theory should work but it doesn't. It fails at [{}] test case. Because for some reason problem did not clarify that the order of brackets is important.
"""

# solution
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(":")","{":"}","[":"]"}
        stack = []
        
        for i in s:
            if i in bracket_dict:
                stack.append(i)
            elif stack and i == bracket_dict[stack[-1]]: # elif stack --> if stack is not empty
                stack.pop()
            else:
                return 0
        return stack == [] # if stack is empty return True, if not return False