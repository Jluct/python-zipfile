from Archivator.ArchiveFile import ArchiveFile


class Archive:
    setting = False
    __archive = False

    def __init__(self, setting):
        # self.__get_os_type()
        self.setting = setting
        # self.__get_catalog()
        self.__archive = ArchiveFile()
        # Инициализация архива ?
        self.__archive.init_archive(self.setting['arch_path'], self.setting['archive_name'])

    def archiving(self):
        # Запись в архив
        self.__archive.archiving(self.setting['files_path'])
        # Закрытие архива
        # self.__archive(self.setting['path'], self.setting['zip_path'])
        pass

    def archiving_additional_files(self):
        if 'additional_files' in self.setting:
            self.__archive.archiving_addition_files(self.setting['additional_files'])

    def inspection_archive(self, name=''):
        return self.__archive.inspection_archive(name)  # !

    def delete_unnecessary_arch(self):
        # self.__archive.delete_unnecessary_arch(self.setting['quantity'])
        pass
