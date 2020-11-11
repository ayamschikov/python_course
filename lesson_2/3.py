# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

months_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
months_dict = {
        0: 'зима',
        1: 'зима',
        2: 'весна',
        3: 'весна',
        4: 'весна',
        5: 'лето',
        6: 'лето',
        7: 'лето',
        8: 'осень',
        9: 'осень',
        10: 'осень',
        11: 'зима'
        }

month_number = int(input('enter month number: ')) - 1

if month_number < 0 or month_number > 11:
    print('month_number must be between 1-12')
    exit()

print(f'season of year by list: {months_list[month_number]}')
print(f'season of year by dict: {months_dict[month_number]}')
