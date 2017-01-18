#**Архиватор**

Модуль создан для резервного копирования веб проектов.


##Настройка
----
```
{
  "proj1": {
    "path": "/home/user/test-dir",
    "quantity": 7,
    "zip_path": "home/user/backup/"
  },
  "proj2": {
    "path": "/home/user/test-dir-1",
    "quantity": 5,
    "zip_path": "home/user/backup/"
  }
}
```

 + **proj1** - блок проекта
 + **path** - путь к проекту
 + **quantity** - количество одновременно существующих резервных копий
 + **zip_path** - адрес хранилица резервных копий


##Использование
----

```
from archive import Archive

# Получаем настройки
setting = json.loads(open('setting.json').read())
# При инициализации передаётся массив с настройками
for key in setting:
    archive = Archive(setting[key])
# Проводим архивацию
    archive.archiving()
# Количество заархивированных файлов
    print(str(archive.files_counter))
# Проверяем количество копий
    archive.inspection_archive()
# Удаляем лишнии копии
    archive.delete_unnecessary_arch()

```

##Планируется
----

+ Добавление функции сохранения архива в облачном хранилище
+ Архивация доп. файлов и папок из сторонних директорий
+ Игнорирования директорий и файлов
+ Чтение файлов типа .gitignore для игнорирования файлов при архивации