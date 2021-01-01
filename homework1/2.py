# написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа
# (выбор производится передачей дополнительного аргумента)

list = []
b = 1
question = int(input('если вы хотите найти чётные, нечётные, или же простые числа, введите 1, 2 или 3 соответсвенно'))
print('вводите целые числа, если хотите закончить ввод, введите 0 :')

while b != 0:
    b = int(input(''))
    list.append(b)
def even(mini_digit):
    for i in range (1, len(list)):
        if i % 2 == 0:
            print(i)

def odd(mini_digit):
    for i in range (1, len(list)):
        if i % 2 == 1:
            print(i)

def simple(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    if counter == 2:
        print(number)

if question == 1:
    even(len(list))

if question == 2:
    odd(len(list))

if question == 3:
    for j in list:
        simple(j)
