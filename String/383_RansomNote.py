"""
If all the letters in ransom note can be picked up from magazine (one letter in magazine could only be used once),
return True, vice versa.

* remember the usage of replace function of string
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        for c in ransomNote:
            if c in magazine:
                magazine=magazine.replace(c, '', 1)
            else:
                return False
        
        return True
