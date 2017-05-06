#!/usr/bin/python3

import os
import random

"""This script generate directory for debug and testing.
    Enter Root directory and directory quantity to generate.
    Files and their contents in these directories can be created randomly or specified by a range of two numbers.

    If your wont generate files in this directories within a certain range
    enter two number (min and max quantity).
    If you do not enter a number, it will be generated automatically in the range from 1 to 10
"""


class Fixture:
    __root_dir = ''
    __count_dir = 10
    __min_files = 1
    __max_files = 10
    __name_dir = 'test-dir-'
    __name_file = 'test-file-'
    __text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce consectetur porta venenatis. Nunc quis sapien quis nunc pharetra mollis. Nullam blandit interdum est ac scelerisque. Phasellus id eros arcu. Fusce in tellus non turpis elementum venenatis sed sit amet arcu. Vestibulum laoreet enim in porttitor tempus. Vestibulum commodo risus in sapien finibus aliquet. Integer sollicitudin, velit in pretium pharetra, velit ipsum ornare massa, quis pretium felis nulla a est. Nunc eget orci in orci fermentum fermentum id vel dui. Vestibulum eget nulla vel sem vehicula pretium nec quis mi. Nullam enim tellus, facilisis vitae nunc sit amet, blandit tempor erat. Suspendisse sit amet leo placerat, bibendum massa sit amet, scelerisque arcu. Phasellus mi lorem, suscipit tincidunt faucibus sed, consectetur eget purus. Morbi fermentum vehicula velit, id aliquam eros semper a. In a lectus sagittis, malesuada massa vel, maximus ligula. Curabitur rutrum mi a posuere bibendum. Integer sodales finibus purus, id dictum ante mattis eu. Donec bibendum purus nisl, a condimentum massa facilisis maximus. Donec sit amet iaculis arcu. Aliquam a ullamcorper urna. Nam at risus porttitor, varius tellus et, mattis neque. Cras vehicula finibus lectus eget eleifend. Nulla interdum sodales arcu sed ullamcorper. Praesent mauris leo, interdum non diam at, imperdiet dictum lacus. Ut eleifend massa non massa consectetur ornare. Sed ultrices bibendum magna, ut eleifend erat tempor nec. Aliquam sit amet venenatis sapien. \n\rДалеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты. Вдали от всех живут они в буквенных домах на берегу Семантика большого языкового океана. Маленький ручеек Даль журчит по всей стране и обеспечивает ее всеми необходимыми правилами. Эта парадигматическая страна, в которой жаренные члены предложения залетают прямо в рот. Даже всемогущая пунктуация не имеет власти над рыбными текстами, ведущими безорфографичный образ жизни. Однажды одна маленькая строчка рыбного текста по имени Lorem ipsum решила выйти в большой мир грамматики. Великий Оксмокс предупреждал ее о злых запятых, диких знаках вопроса и коварных точках с запятой, но текст не дал сбить себя с толку. Он собрал семь своих заглавных букв, подпоясал инициал за пояс и пустился в дорогу. Взобравшись на первую вершину курсивных гор, бросил он последний взгляд назад, на силуэт своего родного города Буквоград, на заголовок деревни Алфавит и на подзаголовок своего переулка Строчка. Грустный реторический вопрос скатился по его щеке и он продолжил свой путь. По дороге встретил текст рукопись. Она предупредила его: «В моей стране все переписывается по несколько раз. Единственное, что от меня осталось, это приставка «и». Возвращайся ты лучше в свою безопасную страну». Не послушавшись рукописи, наш текст продолжил свой путь. Вскоре ему повстречался коварный составитель \n"

    def __init__(self):
        self.__input_date()

    def __input_date(self):
        pass
        self.__root_dir = os.path.normpath(str(input("enter path to root directory (absolute) \n")))
        if self.__root_dir == '' and os.path.isdir(self.__root_dir):
            exit("No enter path or this path not found :(")

        count_dir = input("enter quantity dir \n")
        self.__count_dir = int(count_dir) if count_dir else self.__count_dir

        min_files = input("enter min quantity files \n")
        self.__min_files = int(min_files) if min_files else self.__min_files

        max_files = input("enter max quantity files \n")
        self.__max_files = int(max_files) if max_files else self.__max_files

    def __get_random_number(self):
        return random.randint(self.__min_files, self.__max_files)

    def __generate_dir(self):

        dir_count = self.__count_dir

        while dir_count > 0:
            path = os.path.join(self.__root_dir, self.__name_dir + str(dir_count))

            dir_count -= 1

            if os.path.exists(path):
                self.__generate_files(path)
            else:
                os.makedirs(path)

            self.__generate_files(path)

    def __generate_files(self, path):

        files_count = self.__get_random_number()

        while files_count > 0:
            file = os.path.join(path, self.__name_file + str(files_count) + '.txt')

            self.__generate_file(file)
            files_count -= 1

    def __generate_file(self, file):

        if os.path.isfile(file):
            return False

        f = open(file, 'w+')
        f.write(self.__text)
        f.close()
        return True

    def __get_file_content(self):
        pass

    def run(self):
        self.__generate_dir()

fix = Fixture()
fix.run()
