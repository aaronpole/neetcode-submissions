class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(b+a)
                elif i == '-':
                    stack.append(b-a)
                elif i == '*':
                    stack.append(b*a)
                else:
                    res = abs(b)//abs(a)
                    if (b<0) ^ (a<0):
                        res = -res
                    stack.append(res)
        return stack.pop()
        