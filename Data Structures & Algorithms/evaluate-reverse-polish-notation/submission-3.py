class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        stack = []
        for i in tokens:
            if i in operators:
                sec = stack.pop()
                fir = stack.pop()
                if i == "+":
                    stack.append(fir + sec)
                elif i == "-":
                    stack.append(fir - sec)
                elif i == "*":
                    stack.append(fir * sec)
                else:
                    stack.append(int(fir/sec))
            else:
                stack.append(int(i))
        return stack.pop()