# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X.

# N = int(input('Введите длину массива: '))
# array = list(map(int, input('Введите сам массив: ').split()))
# if len(array) != N or N == 0:
#     print('Введенные элементы не соответствуют заданному количеству!')
# else:
#     X = int(input('Введите число, которое хотите посчитать: '))
#     counter = 0
#     for i in range(N):
#         if array[i] == X:
#             counter += 1
#     print('Чило встречается ', counter, ' раз.')

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X.

# N = int(input('Введите длину массива: '))
# array = list(map(int, input('Введите сам массив: ').split()))
# if len(array) != N or N == 0:
#     print('Введенные элементы не соответствуют заданному количеству!')
# else:
#     X = int(input('Введите число, близкое к которому хотите найти: '))
#     res = 0
#     for i in range(N):
#         check = 100
#         sub = N - array[i]
#         if sub < 0:
#             sub *= -1
#         if check > sub:
#             res = array[i]
#     print('Наиболее близкое число к ', X, ' - это ', res)

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.


english = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
russian = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

N = abs(int(input('Введите 0, используем английскую раскладку, либо 1, если в русскую: ')))
word = input('Введите слово: ').upper()

if N == 0:
	sum = 0
	for letter in word:
		for key, value in english.items():
			if letter in value:
			    sum += key
	print('За это слово вы получаете ', sum, ' очков.')
elif N == 1:
	sum = 0
	for letter in word:
		for key, value in russian.items():
			if letter in value:
			    sum += key
	print('За это слово вы получаете ', sum, ' очков.')
else:
	print('Вы ввели какой-то не тот номер языка, эльфийский мы не обрабатываем...')