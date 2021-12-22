names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
for name in names:
    if name != names[-1]:
        print(name, end = ', ')
print(names[-1])
