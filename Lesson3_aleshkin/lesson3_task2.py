"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
"""
def getuserdata():
    userlist = []
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    yob = input("Введите год рождения: ")
    cob = input("Введите город проживания: ")
    email = input("Введите email: ")
    phone = input("Введите номер телефона: ")
    userlist = (1, {"имя":name, "фамилия":surname, "год рождения":yob, "город проживания":cob, "email":email, "телефон":phone})  
    return userlist

print(getuserdata())
"""
def userdata(name, surname, yob, cob, email, phone):
    print(name, surname, yob, cob, email, phone)

userdata(name= 'Bob', surname='Write', yob=1970, cob='Moscow', email='email@domain.org', phone='0015552321')
