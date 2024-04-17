class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        solution = 0

        for i in range(len(s)): # iterate through all roman numerals
            # roman_dict[s[i]] -> looks for a value of i. character (key) in s str in the dict. (hash map)
            if i < len(s)-1 and roman_dict[s[i]] < roman_dict[s[(i+1)]]: # i < len(s)-1 is required because without it program throws out of bounds exception
                solution -= roman_dict[s[i]]
            else:
                solution += roman_dict[s[i]]
        return solution 
 