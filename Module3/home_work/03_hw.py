import random
numbers = []
n_line = 2
while len(numbers) < n_line:
    numb = random.randint(-100, 100)
    numbers.append(numb)
print(numbers)
summ = 0
for numb in numbers:
    if numb % 2 == 0 and numb > 0:
        summ += numb
print(summ)
