
objects = [['в', 3, 25],
           ['п', 2, 15],
           ['б', 2, 15],
           ['а', 2, 20],
           ['и', 1, 5],
           ['н', 1, 15],
           ['т', 3, 20],
           ['о', 1, 25],
           ['ф', 1, 15],
           ['д', 1, 10],
           ['к', 2, 20],
           ['р', 2, 20]]



points_per_size = []
for i in range(len(objects)):
    points_per_size.append([objects[i][0], objects[i][1], objects[i][2], objects[i][2] / objects[i][1]])

points_per_size.sort(key = lambda j: j[3], reverse = True)

need = [], []       # Предметы
all_points = 0      # Сумма очков выживания
good_points = 10    # Очки выживания предметов
total = 0           # Итого
k = 0
i = 0

for point in range(len(points_per_size)):
    all_points += points_per_size[point][2]


while k < 8:
    indx = i
    i += 1
    if points_per_size[indx][1] == 1:
        need[0].append(points_per_size[indx][0])
        good_points += points_per_size[indx][2]
        k += points_per_size[indx][1]

    if points_per_size[indx][1] == 2:
        need[1].append(points_per_size[indx][0])
        need[1].append(points_per_size[indx][0])
        good_points += points_per_size[indx][2]
        k += points_per_size[indx][1]



for row in need:
    for elem in row:
        print(elem, end = ' ')
    print()

print('Итоговые очки выживания:', good_points - (all_points - good_points))