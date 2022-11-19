#lab3 Ex2
array = ["A","B","C","D","E","F"]
num = []
print(array)

print("\nReverse stack")
for i in range(6):
    num.append(array.pop())
print(num)
