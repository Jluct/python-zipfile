# -*- coding: utf-8 -*-

import json

from archive import Archive

print("Подготовка к архивации")
# print("Проверка прав доступа. Только root может проводить архивацию")
# if os.getlogin() == 'root':
#     print("Всё ОК")
# else:
#     print("Ошибка! Запуск программы осуществлён пользователём " + os.getlogin())
#     exit()

print("Получение настроек")

setting = json.loads(open('setting.json').read())

# print(setting_all)

for key in setting:
    # print(key)
    archive = Archive(setting[key])
    # archive.archiving()
    # print(setting[key])
    # print("Заархивированно " + str(archive.files_counter))
    archive.inspection_archive()
    archive.delete_arch()
print("---------Готово---------")
