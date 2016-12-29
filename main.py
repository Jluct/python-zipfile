# -*- coding: utf-8 -*-

import json

from archive import Archive

setting = json.loads(open('setting.json').read())

for key in setting:
    # print(key)
    archive = Archive(setting[key])
    archive.archiving()
    # print("Заархивированно " + str(archive.files_counter))
    # archive.inspection_archive()
    archive.delete_unnecessary_arch()
print("---------Готово---------")
