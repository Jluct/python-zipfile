
from Archive import ArchiveFile
'''
    В чём прикол, что бы рекурсивно вызвать этот класс нужно передать файл настроек
    Поэтому нужно разнести методы архивации и обработки управления архивацией в разные файлы
    Класс должен обрабатывать только один блок настроек
'''


class Archive:
    setting = False
    __archive = False

    def __init__(self, setting):
        pass
        # self.__get_os_type()
        self.setting = setting
        # self.__get_catalog()
        self.__archive = ArchiveFile(setting.archive_name)

    def archiving(self):
        # Инициализация архива ?

        # Запись в архив по файлам

        # Закрытие архива
        # self.__archive(self.setting['path'], self.setting['zip_path'])
        pass

    def inspection_archive(self):
        pass

    def delete_unnecessary_arch(self):
        pass

    def archiving_additional_files(self):
        pass
