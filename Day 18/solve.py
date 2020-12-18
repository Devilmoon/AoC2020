pred = {'+': 2, '*': 1}

#Shuting Yard Algorithm, returns the expression in reverse polish notation
def sy(exp, part2=False):
    out = []
    opstack = []
    for char in exp:
        #read a token.
        if char.isnumeric():
            out.append(char)
        elif char == '+' or char == '*':
            if not part2:
                while (len(opstack)>0 and opstack[-1]!='('):
                    out.append(opstack.pop())
                opstack.append(char)
            else:
                while (len(opstack)>0 and opstack[-1]!='(' and pred[opstack[-1]] >= pred[char]):
                    out.append(opstack.pop())
                opstack.append(char)
        elif char == "(":
            opstack.append(char)
        elif char == ")":
            while opstack[-1]!='(':
                out.append(opstack.pop())
            # If the stack runs out without finding a left parenthesis, then there are mismatched parentheses.
            if opstack[-1]=='(':
                opstack.pop()
    # After while loop, if operator stack not null, pop everything to output queue
    while opstack:
        # If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses.
        out.append(opstack.pop())
    return out

def calculate(rpn):
    stack = []
    for char in rpn:
        if char.isnumeric():
            stack.append(char)
        elif char == '*' or char == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            r = a * b if char == '*' else a + b
            stack.append(r)
    return stack.pop()

total=0
total2=0
with open('input.txt') as f:
    for line in f:
        total+=calculate(sy(line.strip()))
        total2+=calculate(sy(line.strip(), part2=True))
print('Part 1: {}'.format(total))
print('Part 2: {}'.format(total2))
