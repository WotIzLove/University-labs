#Обувная фабрика собирается начать выпуск элитной модели ботинок. Дырочки для шнуровки будут расположены в два ряда, расстояние между рядами равно a, а расстояние между дырочками в ряду b. Количество дырочек в каждом ряду равно N. Шнуровка должна происходить элитным способом “наверх, по горизонтали в другой ряд, наверх, по горизонтали и т.д.” (см. рисунок). Кроме того, чтобы шнурки можно было завязать элитным бантиком, длина свободного конца шнурка должна быть l. Какова должна быть длина шнурка для этих ботинок?

a = int(input())
b = int(input())
l = int(input())
N = int(input())

print(2 * (N * (a + b) + l - b) - a)