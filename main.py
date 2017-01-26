# -*- coding: utf-8 -*-

import json

from Archivator.Archive import Archive

setting = json.loads(open('setting.json').read())

for key in setting:
    archive = Archive(setting[key])
    archive.archiving()
    archive.archiving_additional_files()
    print(archive.inspection_archive())
    archive.delete_unnecessary_arch()
print("---------Готово---------")
