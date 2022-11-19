#lab3 Ex1
array = ["A","B","C","D","E","F"]
Stack = []
print(array)
print("\n")
Stack.append("A")
print(Stack)
Stack.append("B")
print(Stack)
Stack.append("C")
print(Stack)
Stack.append("D")
print(Stack)
Stack.append("E")
print(Stack)
Stack.append("F")
print(Stack)

print("\nFirst in last out ")
for i in range(6):
        n = Stack[-1]
        Stack.pop()
        print(Stack)
        
print("\nFirst in First out ")
Stack.append("A")
print(Stack)
Stack.append("B")
print(Stack)
Stack.append("C")
print(Stack)
Stack.append("D")
print(Stack)
Stack.append("E")
print(Stack)
Stack.append("F")
print(Stack)

print("\nFirst in First out ")
for i in range(6):
        n = Stack[-1]
        Stack.pop(0)
        print(Stack)
