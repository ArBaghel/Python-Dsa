# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
#s consists only of printable ASCII characters.
import string
class Solution:
    def isalphanumeric(self,s):
        x=ord(s)
        if 97<=x<=122 or 65<=x<=90 or 48<=x<=57:
            return True
        return False
    def isPalindrome(self, s: str) ->bool:
        s=s.lower()
        i,j=0,len(s)-1
        while i<j:
            if not self.isalphanumeric(s[i]):
                i+=1
            elif not self.isalphanumeric(s[j]):
                j-=1
            elif s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False    
        return True