from datetime import datetime

class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed
    
    def push(self, item):
        self.stack.append(item)

start_time = datetime.now()
letter = Stack()
nums = Stack()
left_simbols = Stack()
print("Строка - ", open("line.txt", "r").read())
f = open("line.txt", "r")
fd = f.readlines()
for i in fd:
    for j in i:
        if j.isalpha():
            letter.push(j)
        elif j.isdigit():
            nums.push(j)
        else:
            left_simbols.push(j)


print("Стек букв - ", letter.stack)
print("Стек цифр - ", nums.stack)
print("Стек символов - ", left_simbols.stack)
for i in range(len(letter.stack)):
    print(letter.stack[i], end="")
for i in range(len(nums.stack)):
    print(nums.stack[i], end="")
for i in range(len(left_simbols.stack)):
    print(left_simbols.stack[i], end="")

print("\nВермя выполнения - ", datetime.now()-start_time)
input("Нажмите для продолжения...")
