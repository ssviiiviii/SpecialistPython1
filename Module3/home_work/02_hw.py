import random
numbers = []
n_line = 20
while len(numbers) < n_line:
    numb = random.randint(-100, 100)
    numbers.append(numb)
print(numbers)
