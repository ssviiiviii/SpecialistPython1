number_of_cows = int(input('На лугу пасется... '))
num = number_of_cows % 10 
if num == 1:
    print(number_of_cows, 'корова')
elif num == 2 or num == 3 or num == 4:
    print(number_of_cows, 'коровы')
else:
    print(number_of_cows, 'коров')
