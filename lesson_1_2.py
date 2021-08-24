#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

#data = int(input("Пожалуйста, введите время в секундах: "))
data = 9840
hour = data // 3600
minutes = (data % 3600) // 60
second = (data % 3600) - (minutes * 60)
hour = str(hour)
minutes = str(minutes)
second = str(second)
print(f'{hour:} : {minutes:.02} : {second}')