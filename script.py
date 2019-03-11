# Все числа целые положительные. 100 ≤ K1, K2 ≤ 30000 (кратное 100), 0 ≤ L1, L2 ≤ 100, 1 ≤ P1, P2 ≤ 100
# 1000 - начальное число шприцов    0 - процент потерянных шприцов  1 - стоимость одного шприца
# 1000 - начальное число игл        1 - процент потерянных игл      1 - стоимость одного иглы
inp = open('2/input.txt')
data = [a.split() for a in inp.readlines()]
for i in range(len(data)):
    row = data[i]
    if 100 <= int(row[0]) <= 30000 and int(row[0]) % 100 == 0:
        if 0 <= int(row[1]) <= 100:
            if 1 <= int(row[2]) <= 100:
                print('Good Row')
                continue
    print('Bad Row')
    break
else:
    print('\nERROR')


