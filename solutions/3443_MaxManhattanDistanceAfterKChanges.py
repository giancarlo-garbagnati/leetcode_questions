""" https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/description/
Not a complete solution (only solved 649/828 testcases) but putting a pin in 
this to possibly use later (since I want to move on and practice other qs).

Some things I think I did decently was:
1) Short circuiting much of the testcases by checking if number of changes is
more than the "minority" directions
2) Calculating a "change list" (although ultimately flawed) for which letter to
prioritize changing based on the surrounding circumstance.
"""
################################################################################
""" https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/description/
3443. Maximum Manhattan Distance After K Changes
Attempted
Medium
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
 

Example 1:

Input: s = "NWSE", k = 1

Output: 3

Explanation:

Change s[2] from 'S' to 'N'. The string s becomes "NWNE".

Movement	Position (x, y)	Manhattan Distance	Maximum
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

Example 2:

Input: s = "NSWWEW", k = 3

Output: 6

Explanation:

Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".

The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

 

Constraints:

1 <= s.length <= 105
0 <= k <= s.length
s consists of only 'N', 'S', 'E', and 'W'.
"""

class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # calculate deviancy from majority and majority directions
        d_counts = {
            'N':0,
            'W':0,
            'S':0,
            'E':0
        }
        for c in s:
            d_counts[c] += 1
        
        if d_counts['N'] >= d_counts['S']:
            lat_dir = 'N'
            lat_min = 'S'
        else:
            lat_dir = 'S'
            lat_min = 'N'
        if d_counts['W'] >= d_counts['E']:
            lon_dir = 'W'
            lon_min = 'E'
        else:
            lon_dir = 'E'
            lon_min = 'W'

        if d_counts[lat_min] + d_counts[lon_min] <= k:
            return len(s)
        lat_diff = d_counts[lat_dir] - d_counts[lat_min]
        lon_diff = d_counts[lon_dir] - d_counts[lon_min]

        l = list(s)
        list_of_mins = [] # [major_str_len, index, letter_to_change_to] # will sort by [0]
        for i, c in enumerate(l):
            if c in [lat_min, lon_min]:
                if c == lat_min:
                    c_change = lat_dir
                else: # c == lon_min
                    c_change = lon_dir
                
                major_str_len = 0
                # before
                for c2 in l[:i][::-1]: # first part of the string before i, but reversed
                    if c2 == c_change:
                        major_str_len += 1
                    elif c2 == c:
                        break
                # after
                for c2 in l[i+1:]:
                    if c2 == c_change:
                        major_str_len += 1
                    elif c2 == c:
                        break

                list_of_mins.append([major_str_len, i, c_change])

        list_of_mins = sorted(list_of_mins, key=lambda x: (-x[0],x[1],x[2]))
        print(list_of_mins)

        for _ in range(k):
            changes = list_of_mins.pop(0)
            l[changes[1]] = changes[2]

        # calc max_man_dist
        max_man_dist = 0
        origin = [0,0]
        current = [0,0]
        for c in l:
            if c == 'N':
                current[1] += 1
            elif c == 'S':
                current[1] -= 1
            elif c == 'E':
                current[0] += 1
            else: # c == 'W'
                current[0] -= 1
            
            man_dist = abs(current[0]-origin[0]) + abs(current[1]-origin[1])

            if man_dist > max_man_dist:
                max_man_dist = man_dist

        return max_man_dist
