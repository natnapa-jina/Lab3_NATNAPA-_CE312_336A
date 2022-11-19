#lab3 Ex3
input = ["A","+","B"]
print("infix =",input)
stack= []
input.reverse()
operators = set(['+', '-', '*', '/', '^'])

for i in input:
    if i in operators:
        a = stack.pop()
        b = a+i
        stack.append(b)
    else:
        stack.append(i)
stack.reverse()
print("postfix =",*stack)
