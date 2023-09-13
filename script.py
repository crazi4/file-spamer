#Сделано пользователем crazi4
#Источник:
#https://github.com/crazi4/file-spamer
#Если есть вопросы, пишите в телеграм @crazi444

from random import randint
import os
import getpass

list = open('list.txt', 'r')
main = os.getcwd()
user = getpass.getuser()
desktop = ("C:/Users/" + user + "/Desktop")


a = int(input("Сколько тысяч символов? (0 - бесконечно): "))
b = int(input("Кол-во файлов: "))
c = 1

os.chdir(desktop)
if not os.path.isdir("LolKek12"):
    os.mkdir("LolKek12")

work = (desktop + "/LolKek12")


if a < 0 or b < 1:
    print("Введите корректное число! Перезапустите программу.")
else:
    print("Добавление...")
    for i in range(b):
        os.chdir(main)
        list = open('list.txt', 'r')
        os.chdir(work)
        file = open(str(c) + '.txt', 'w')
        file.write(list.read() * a * 50)
        file.close()
        c += 1
        print("Успешно создан", c - 1,"файл.")
            
print("Все файлы созданы. Вы можете закрыть программу.")
input()
