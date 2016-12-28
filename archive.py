import zipfile
import os
import sys
import datetime


class Archive:
    setting = False
    parent_catalog = False
    files_counter = 0
    catalog = ''
    separator = "|"

    def __init__(self, setting):
        if not setting:
            print("Нет настроек для архивации")
        self.setting = setting
        self.__get_catalog()

    def __get_catalog(self):
        self.catalog = (self.setting['path']).split('/')[-1]

    def __get_parent_catalog(self):
        return (self.setting['path']).split(self.catalog)[0]

    def __init_archive(self):
        name = self.setting['zip_path'] + self.catalog + self.separator + \
               str(datetime.datetime.now().__format__('%d.%m.%Y %H:%M:%S')) + ".zip"
        return zipfile.ZipFile(name, 'w')

    def __get_catalog_content(self):
        return os.walk(self.setting['path'])

    def __get_os_type(self):
        if sys.platform == 'win32':
            return '\\'
        else:
            return '/'

    def archiving(self):

        content = self.__get_catalog_content()
        parent_catalog = self.__get_parent_catalog()
        arch = self.__init_archive()

        os_sym = self.__get_os_type()

        for root, dirs, files in content:
            for file in files:
                current_dir = root.split(parent_catalog)[-1] + os_sym
                print("Архивация " + current_dir + " " + str(files))
                arch.write(os.path.join(current_dir, file))
                self.files_counter = self.files_counter + 1

        arch.close()

    def inspection_archive(self):
        arch_counter = 0
        data_files = os.listdir(self.setting['zip_path'])
        for value in data_files:
            if value.find(self.catalog + self.separator) != (-1):
                arch_counter = arch_counter + 1
                # print(arch_counter)
        return arch_counter
        # print(str(data_files))
    def delete_arch(self):

        data = {}
        data_files = os.listdir(self.setting['zip_path'])
        for value in data_files:
            if value.find(self.catalog + self.separator) != (-1):
                str_date = str((value.split(self.separator)[1]).split('.zip')[0])
                data[value] =  datetime.datetime.strptime(str_date, '%d.%m.%Y %H:%M:%S')

        print(str(data))

