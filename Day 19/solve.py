import re
from lark import Lark


with open('input.txt') as f:
  grammar, inputs = f.read().split('\n\n')

part2 = False
if part2:
    grammar = grammar.replace('8: 42', '8: 42 | 42 8')
    grammar = grammar.replace('11: 42 31', '11: 42 31 | 42 11 31')

lgrammar = []
for line in grammar.splitlines():
    line = re.sub(r"(\d+)", r"s\1", line)
    lgrammar.append(line)
lgrammar.append('start: s0')
lgrammar = '\n'.join(lgrammar)

l = Lark(lgrammar)
cnt = 0
for input in inputs.splitlines():
    try:
        l.parse(input)
        cnt += 1
    except:
        pass

print(cnt)