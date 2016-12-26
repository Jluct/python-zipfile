import zipfile
import os
import sys
import datetime


class Archive:
    setting = False
    parent_catalog = False
    files_counter = 0

    def __init__(self, setting):
        if not setting:
            print("Нет настроек для архивации")
        self.setting = setting

    def __get_catalog(self):
        return (self.setting['path']).split('/')[-1]

    def __get_parent_catalog(self):
        return (self.setting['path']).split(self.__get_catalog())[0]

    def __init_archive(self):
        name = self.setting['zip_path'] + 'backup|' + str(datetime.datetime.now()) + ".zip"
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
