from Archivator.ArchiveFile import ArchiveFile


class Archive:
    setting = False
    __archive = False

    def __init__(self, setting):
        # self.__get_os_type()
        self.setting = setting
        # self.__get_catalog()
        self.__archive = ArchiveFile()

    def archiving(self):
        # Инициализация архива ?
        self.__archive.init_archive(self.setting['archive_name'])

        # Запись в архив по файлам
        self.__archive.archiving(self.setting['path'])
        # Закрытие архива
        # self.__archive(self.setting['path'], self.setting['zip_path'])

    def inspection_archive(self):
        self.__archive.inspection_archive()  # !

    def delete_unnecessary_arch(self):
        self.__archive.delete_unnecessary_arch(self.setting['quantity'])

    def archiving_additional_files(self):
        pass
