class Solution:
    def isValid(self, s: str) -> bool:
        stack, mp = [], {')':'(',']':'[','}':'{'}
        for i in s:
            if i in mp.values():
                stack.append(i)
            elif not stack or stack.pop() != mp[i]:
                return False
        return not stack
        