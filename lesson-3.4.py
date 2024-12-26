# 1.
def numbers(n):

    total = 0
    for i in range(1, n + 1):
        total += i
    return total


yoda = int(input("Введите число n: "))

if yoda < 1:
    print("Пожалуйста, введите положительное целое число.")
else:
    result = numbers(yoda)
    print(f"Сумма всех чисел от 1 до {yoda} равна {result}.")

# 2.
banana = [1, 2, 3, 4, 5, 6]
avocados = []
zombies = []
for n in banana:
    if n % 2 == 0:
        avocados.append(n)
    else:
        zombies.append(n)
print("Чётные:", avocados)
print("Нечётные:", zombies)

# 3.
yoda = int(input("Введите число n: "))
factorial_result = 1
factorial_str = ""

for i in range(yoda, 0, -1):

    factorial_result *= i
    factorial_str += str(i) + "*"
factorial_str = factorial_str[:-1]

print(f"{yoda}! = {factorial_result} ({factorial_str})")

# 4
input_str = input("Введите числа через запятую: ")
num = [int(num) for num in input_str.replace(" ", "").split(",")]

big_daddy = max(num)
tiny_bean = min(num)

print("Big Daddy:", big_daddy)
print("Tiny Bean:", tiny_bean)

# 5
nash_boom = 1234
ozon = sum(int(digit) for digit in str(nash_boom))

print("Сумма цифр:", ozon)

# 6
puzzle_pieces = [3, 5, 3, 7, 5, 5, 3]

count_pieces = {}
for piece in puzzle_pieces:
    count_pieces[piece] = count_pieces.get(piece, 0) + 1
print(count_pieces)

# 7.
numbers = [1, 2, 3, 4, 5, 6]
tiny_monsters = [num for num in numbers if num % 2 != 0]


print("Нечётные монстры:", tiny_monsters)


# 8
fruits = ["apple", "kiwi", "banana", "cherry"]
min_length = 4

big_fruits = [fruit for fruit in fruits if len(fruit) > min_length]
print("Большие фрукты:", big_fruits)


# 9
numbers = [-5, 3, 1, 4, 2, -6]
happy_numbers = [num for num in numbers if num > 0]
grumpy_numbers = [num for num in numbers if num < 0]

print("Счастливые числа:", happy_numbers)
print("Суровые числа:", grumpy_numbers)

# 10
yoda = 4
word_count = sum(1 for fruit in fruits if len(fruit) > yoda)

print(f"Количество слов, длиннее чем {yoda} символов: {word_count}")
