side_a = int(input('Введите первую сторону: '))
side_b = int(input('Введите вторую сторону: '))
side_c = int(input('Введите третью сторону: '))
if side_a + side_b == side_c or (side_b + side_c == side_a) or (side_a + side_c == side_b):
    print('YES')
else:
    print('NO')
