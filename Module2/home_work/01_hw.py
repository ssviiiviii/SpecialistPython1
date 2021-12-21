choco_side_1 = int(input('Введите ширину шоколада: '))
choco_side_2 = int(input('Введите длинну шоколада: '))
piece = int(input('введите кол-во кусочков шоколада: '))
piece_of_chocolate = (choco_side_1 * choco_side_2) - piece
if piece_of_chocolate % choco_side_1 == 0 or piece_of_chocolate % choco_side_2 == 0:
    print('yes')
else:
    print('no')
