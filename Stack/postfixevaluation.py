class Postfix_result:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return True if self.stack == [] else False
    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return

    def push(self, x):
        self.stack.append(x)

    def Postfix_solve(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                x=self.pop()
                y=self.pop()
                self.push(str(eval(y+i+x)))


        return int(self.pop())

expression=input()
ans=Postfix_result()
print(ans.Postfix_solve(expression)) # postfix evaluation

