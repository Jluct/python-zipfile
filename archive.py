import zipfile
import os
import sys
import datetime


class Archive:
    setting = False
    parent_catalog = False
    files_counter = 0
    catalog = ''
    separator = ".-."
    path_separator = "/"
    datetime_format = '%d.%m.%Y %H:%M:%S'

    def __init__(self, setting):

        self.__get_os_type()
        self.setting = setting
        self.__get_catalog()

    def archiving(self):

        content = self.__get_catalog_content()
        parent_catalog = self.__get_parent_catalog()
        arch = self.__init_archive()

        for root, dirs, files in content:
            for file in files:
                current_dir = root.split(parent_catalog)[-1] + str(self.path_separator)
                arch.write(os.path.join(current_dir, file))
                self.files_counter = self.files_counter + 1

        arch.close()

    def inspection_archive(self):
        arch_counter = 0
        data_files = os.listdir(self.setting['zip_path'])
        for value in data_files:
            if value.find(self.catalog + self.separator) != (-1):
                arch_counter = arch_counter + 1

        return arch_counter

    def delete_unnecessary_arch(self):
        arch = self.__sorted_arch()
        count = len(arch) - self.setting['quantity']
        if count <= 0:
            return True

        i = 0

        while i < count:
            os.remove(self.setting['zip_path'] + arch[i])
            i = i + 1

    def __sorted_arch(self):
        data = {}
        data_sortable = []
        data_files = os.listdir(self.setting['zip_path'])
        for value in data_files:
            if value.find(self.catalog + self.separator) != (-1):
                str_date = str((value.split(self.separator)[1]).split('.zip')[0])
                data[value] = int(datetime.datetime.strptime(str_date, self.datetime_format).timestamp())

        for key in sorted(data):
            data_sortable.append(key)

        return data_sortable

    def __get_catalog(self):
        self.catalog = (self.setting['path']).split(self.path_separator)[-1]

    def __get_parent_catalog(self):
        return (self.setting['path']).split(self.catalog)[0]

    def __init_archive(self):
        name = self.setting['zip_path'] + self.catalog + self.separator + str(
            datetime.datetime.now().__format__(self.datetime_format)) + ".zip"
        return zipfile.ZipFile(name, 'w')

    def __get_catalog_content(self):
        return os.walk(self.setting['path'])

    def __get_os_type(self):
        if sys.platform == 'win32':
            self.path_separator = '\\'
            self.datetime_format = '%d.%m.%Y %H-%M-%S'
