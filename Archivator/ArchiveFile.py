import zipfile
import os
import sys
import datetime


class ArchiveFile:
    # Родительский каталог архива, что бы получились относительные пути
    parent_archive = False

    # Количество заархивированных файлов
    files_counter = 0

    # Каталог с архивируемыми файлами
    catalog = ''

    # Символ разделителя файловой системы. По умолчанию UNIX
    path_separator = "/"

    # Символ отделения названия в архиве. Состоит из названия каталога+separator+дата и время архивации
    separator = ".-."

    # дата и время архивации
    datetime_format = '%d.%m.%Y %H:%M:%S'

    # Путь к архивируемым файлам
    files_path = ''

    # Путь к директории для архива
    arch_patch = ''

    # Архив
    path_arch = ''

    # Базовое название архива
    __arch_name = ''

    # Ресурс архива
    __archive = False

    """Получение настроек для ОС
        Получение название каталога с файлами
    """

    def __init__(self, archive_path=False, archive_mode="a"):
        self.__get_os_type()

        if (archive_path != False):
            self.__archive = self.open_archive(archive_path, archive_mode)


            # self.__get_catalog()

    def init_archive(self, arch_patch, arch_name=""):

        self.arch_patch = arch_patch
        self.__arch_name = arch_name

        name = self.arch_patch + arch_name + self.separator + str(
            datetime.datetime.now().__format__(self.datetime_format)) + ".zip"
        self.__archive = zipfile.ZipFile(name, 'w')

        self.path_arch = name

        return self

    def archiving(self, files_path):

        self.files_path = files_path

        content = self.__get_catalog_content(files_path)  # !
        parent_catalog = self.__get_parent_catalog(files_path)  # !
        # print(parent_catalog)

        # переход в родительский каталог архива
        os.chdir(parent_catalog)

        for root, dirs, files in content:
            for file in files:
                current_dir = root.split(parent_catalog)[-1] + self.path_separator
                # print(os.path.join(current_dir, file))

                self.__archive.write(os.path.join(current_dir, file))
                self.files_counter = self.files_counter + 1

        self.close_archive()

    def close_archive(self):
        self.__archive.close()

    def open_archive(self, archive_path, archive_mode):

        if zipfile.is_zipfile(archive_path):
            return zipfile.ZipFile(archive_path, archive_mode)
        else:
            return False

    def archiving_addition_files(self, array_files):

        print(type(self.__archive))
        self.__archive = self.open_archive(self.path_arch, 'a')
        print(type(self.__archive))

        # os.mkdir(self.path_arch + self.path_separator + 'additional_files' + self.path_separator)

        i = 0
        while i < len(array_files):

            if os.path.isdir(array_files[i]):
                self.archiving(array_files[i])
            elif os.path.isfile(array_files[i]):
                parent_catalog = self.__get_parent_catalog(array_files[i])
                os.chdir(parent_catalog)

                file = array_files[i].split(parent_catalog)[-1]

                self.__archive.write(file)

            i = i + 1

        self.close_archive()

    def inspection_archive(self, arch_name=False):

        if (arch_name is not True) and (self.__arch_name == ''):
            return False

        if arch_name is not True:
            arch_name = self.__arch_name

        arch_counter = 0
        data_files = os.listdir(self.arch_patch)

        print(data_files)

        for value in data_files:
            if value.find(arch_name + self.separator) != (-1):
                arch_counter = arch_counter + 1

        return arch_counter

    #
    # def delete_unnecessary_arch(self, quantity):
    #     arch = self.__sorted_arch()
    #     count = len(arch) - quantity
    #     if count <= 0:
    #         return True
    #
    #     i = 0
    #
    #     while i < count:
    #         os.remove(self.arch_patch + arch[i])
    #         i = i + 1
    #
    # def __sorted_arch(self):
    #     data = {}
    #     data_sortable = []
    #     data_files = os.listdir(self.arch_patch)
    #     for value in data_files:
    #         if value.find(self.catalog + self.separator) != (-1):
    #             str_date = str((value.split(self.separator)[1]).split('.zip')[0])
    #             data[value] = int(datetime.datetime.strptime(str_date, self.datetime_format).timestamp())
    #
    #     for key in sorted(data):
    #         data_sortable.append(key)
    #
    #     return data_sortable

    def __get_catalog_content(self, files_path):
        return os.walk(files_path)

    def __get_os_type(self):
        if sys.platform == 'win32':
            self.path_separator = '\\'
            self.datetime_format = '%d.%m.%Y %H-%M-%S'

    """Возвращает название каталога архивируемой папки"""

    def __get_catalog(self, files_path):
        return files_path.split(self.path_separator)[-1]

    """Возвращает родительский каталог архивируемой папки"""

    def __get_parent_catalog(self, files_path):
        return files_path.split(self.__get_catalog(files_path))[0]
