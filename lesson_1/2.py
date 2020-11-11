# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
seconds = int(input('enter number of seconds: '))

hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds = seconds - hours * 3600 - minutes * 60

print('formatted time - {}:{}:{}'.format(hours, minutes, seconds))
