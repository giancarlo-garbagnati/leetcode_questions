"""
1249. Minimum Remove to Make Valid Parentheses
Medium

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.

"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        return_str = []
        last_open_parens = []
        net_paren = 0 # subtract for )s, add for (s
        deletions = 0
        for i, c in enumerate(list(s)):
            if c not in ['(',')']:
                return_str += c
            elif c == ')':
                net_paren -= 1
                if net_paren < 0: # deletion
                    net_paren = 0 
                    deletions += 1
                    continue
                else:
                    return_str.append(c)
                    last_open_parens.pop()
            else: # c == '('
                net_paren += 1
                return_str.append(c)
                last_open_parens.append(i)
        
        for _ in range(net_paren):
            rindex = last_open_parens.pop()
            return_str.pop(rindex-deletions)
            
        return ''.join(return_str)

"""
Test cases
Case 1:
Input
s =
"lee(t(c)o)de)"
Output
"lee(t(c)o)de"
Expected
"lee(t(c)o)de"

Case 2:
Input
s =
"a)b(c)d"
Output
"ab(c)d"
Expected
"ab(c)d"

Case 3:
Input
s =
"))(("
Output
""
Expected
""

"""
