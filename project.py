# print(8 / 2 + 5 - (-3) / 2)
from random import random

# print(70 * (3 + 4) / (8 + 2))

# print(0.39 * 0.22)

# print(5 ** 2 - 3 * 7)

# Символ экранирования  \
# print("\"Khal Drogo's favorite word is \"athjahakar\"\"")

# Энкранированая последовательность \n
# print("- Did Joffrey agree?\n- He did. He also said \"I love using \\n\".")

# Конкатенация
# print("Winter" + " came" + " for" + " the" + " House" + " of" + " Frey.")

# f"{test}" - Интерполяция


# print(chr(126)); print(chr(94)); print(chr(37))

# motto = "What Is Dead May Never Die!"
# print(motto)

# name = 'Brienna'
# name = 'anneirB'
# print(name)

# countBrothers = 2
# print(countBrothers)

# family = "Targaryen"
# pet = "Dragon"

# print(family)
# print(' and ')
# print(pet)

# eurosCount = 100
# dollarsCount = eurosCount * 1.25
# yuan'sCount = dollarsCount * 6.91

# print(f"{dollarsCount}\n{yuan'sCount}")


# info = "We couldn't verify your mother's maiden name."
# intro = "Here is important information about your account security."
# first_name = 'Joffrey'
# greeting = 'Hello'

# print(greeting + ", " + first_name + "!")
# print(intro + "\n" + info)


# first_number = 20
# second_number = -100
# print(first_number * second_number)

# castle_count = 6
# room_count = 17
# king = "Rooms in King Balon's Castle:"

# print(king + f"\n{castle_count * room_count}")

# DRAGONS_BORN_COUNT = 3
# print(DRAGONS_BORN_COUNT)

# stark = 'Arya'
# print(f"Do you want to eat, {stark}?")

# name = 'Na\nharis'
# print(name[-1])


# value = 'Hexlet'
# print(value[2:5])

# text = '''Lannister, Targaryen, Baratheon, Stark, Tyrell...
# they're all just spokes on a wheel.
# This one's on top, then that one's on top, and on and on it spins,
# crushing those on the ground.'''

# print(text)


# Неизменяемость примитивных типов

# one = 'Naharis'
# two = 'Mormont'
# three = 'Sand'

# print(f"\n{one[2]}{two[1]}{three[-1]}{two[-3]}{two[2]}")




# Явное преобразование типов

# Вариант 1
# value = str(2.9)

# print(f"{value[0]} times")

# Вариант 2
# value = 2.9
# int_value = int(value)
# str_value = str(int_value)

# print(str_value + " times")

# Функции и их вызов

# Вариант 1
# company1 = 'Apple'
# company2 = 'Samsung'

# print(len(company1) + len(company2))

# Вариант 2
# company1 = 'Apple'
# company2 = 'Samsung'

# company1_len = len(company1)
# company2_len = len(company2)

# print(company1_len + company2_len)

# number = 255
# number_hex = hex(number)

# print(number_hex)

# number = 10.1234
# number_round = round(number, 2)

# print(number_round)

#Выведите на экран первую и последнюю буквы предложения,
#записанного в переменную text, в следующем формате:
# First: N
# Last: t

# text = 'Never forget what you are, for surely the world will not'
# result = f"First: {text[0]}\nLast: {text[-1]}"
# print(result)

# a = [3, 10, 22, -3, 0]
# print(min(a))


# Детерминированность / Недетерминированность
#print(round(random() * 10))

# motto = 'Family, Duty, Honor'
# print(type(motto))

# text = 'a MIND needs Books as a Sword needS a WHETSTONE.'
# lower_text = text.lower()

# print(lower_text)



# first_name = '  Grigor   \n'
# first_name = first_name.strip()
# print(first_name)

# Index Of N: 0
# Index Of ,: 25

#???????????????
# text = 'Never forget what you are, for surely the world will not'

# print(f"Index Of N: {text.find("N")}\nIndex Of ,: {text.find(",")}")
# print(f'Index Of N: {text.find("N")}\nIndex Of ,: {text.find(",")}')

# text = 'Never forget what you are, for surely the world will not'
# print("Index Of N: " + str(text.find("N")) + "\nIndex Of ,: " + str(text.find(",")))

# text = 'When \t\n you play a \t\n game of thrones you win or you die.'
# print(text[5:15].strip().__len__())

#print_motto() => Winter is coming

#Определение функции
# def print_motto():
#     print("Winter is coming")
# print_motto()

# def say_hurray_three_times():
#    text = "hurray! hurray! hurray!"
#    return text

# print(say_hurray_three_times())
