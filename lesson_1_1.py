# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = 'Alex'
age = 20
city = 'Moscow'
country = 'Russia'

print(f"Привет {name}. Я знаю что тебе {age} лет, живёшь в городе {city}, что столицей родины нашей является, именуемой {country}.")

name = input("Пожалуйста, введите имя: ")
age = int(input("Возраст: "))
city = input("Город проживания: ")
country = input("Страна: ")

print(f"Привет {name}. Я знаю что тебе {age} лет, живёшь в {city}, что столицей родины нашей является, именуемой {country}.")

name = "Родион"
print("Приятно познакомиться. А меня зовут " + name + ".")