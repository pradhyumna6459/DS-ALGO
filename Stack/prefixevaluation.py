class Prefix_result:
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

    def Prefix_solve(self, exp):
        exp=exp[::-1]
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                x=self.pop()
                y=self.pop()
                self.push(str(eval(x+i+y)))


        return int(self.pop())

expression=input()
ans=Prefix_result()
print(ans.Prefix_solve(expression)) # prefix evaluation

