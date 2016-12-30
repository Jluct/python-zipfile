# -*- coding: utf-8 -*-

import json

from archive import Archive

setting = json.loads(open('setting.json').read())

for key in setting:
    archive = Archive(setting[key])
    archive.archiving()
    # print(str(archive.files_counter))
    # archive.inspection_archive()
    archive.delete_unnecessary_arch()
print("---------Готово---------")
