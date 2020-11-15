# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_info(name='', last_name='', year='', city='', email='', phone=''):
    print(f"User {name} {last_name} was born in {year}, lives in {city}, email - {email}, phone - {phone}")

name = input('name: ')
last_name = input('last_name: ')
year = input('year: ')
city = input('city: ')
email = input('email: ')
phone = input('phone: ')

user_info(name=name, year=year, last_name=last_name, email=email, phone=phone, city=city)
