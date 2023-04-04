import os
import zipfile
from os.path import basename

current_dir = os.path.dirname(__file__)
path_xlsx = os.path.abspath('Financial Sample.xlsx')

path_files = os.path.join(current_dir, '..', 'resources')
file_dir = os.listdir(path_files)

with zipfile.ZipFile('..\\resources\\myZip.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    for files in file_dir:
        add_files = os.path.join(path_files, files)
        my_zip.write(add_files, basename(add_files))

with zipfile.ZipFile('..\\resources\\myZip.zip', mode='a', compression=zipfile.ZIP_DEFLATED) as add_zip:
    add_zip.write(path_xlsx, basename(path_xlsx))

current_dir = os.path.dirname(os.path.abspath(__file__))
create_sours = os.path.abspath(os.path.join(current_dir, '..', 'resources'))
