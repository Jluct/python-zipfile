# -*- coding: utf-8 -*-
import zipfile
import os
import datetime
import json

# print("Подготовка к архивации")
# print("Проверка прав доступа. Только root может проводить архивацию")
# if os.getlogin() == 'root':
#     print("Всё ОК")
# else:
#     print("Ошибка! Запуск программы осуществлён пользователём " + os.getlogin())
#     exit()

# print("Получение настроек")

setting = json.loads(open('setting.json').read())
current_date = datetime.datetime.now()
# print(current_date)


catalog_list = os.listdir(setting['path'])
# print("Выбранный каталог")
catalog = (setting['path']).split('/')[-1]
catalog_parent = (setting['path']).split(catalog)[0]
os.chdir(catalog_parent)
# print(catalog)
# print(catalog_parent)
# print(catalog_list)

name = setting['zip_path'] + 'test|' + str(current_date) + ".zip"

# print("Подготовка архива")

arch = zipfile.ZipFile(name, 'w')

# print("Запись в архив папки")
# print(name)

user_dir = os.walk(setting['path'])
files_counter = 0
for root, dirs, files in user_dir:
    for file in files:
        my_dir = root.split(catalog_parent)[-1] + "/"
        print("Архивация " + my_dir + " " + str(files))
        arch.write(os.path.join(my_dir, file))
        files_counter = files_counter + 1
arch.close()

print("Заархивированно " + str(files_counter))
print("---------Готово---------")
