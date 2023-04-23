import os
import zipfile
from os.path import basename
from pathlib import Path
import way_qa_guru_python_4_7


def project():
    return Path(way_qa_guru_python_4_7.__file__).parent  # Находит путь где лежит проект


def resources():
    return str(project().joinpath(f'resources/'))  # от проекта находит путь где лежит папка resources/

this_dir = os.path.dirname(__file__)
path_xlsx = os.path.abspath('Financial Sample.xlsx')

path_files = os.path.join(os.path.dirname(this_dir), 'resources')
file_dir = os.listdir(path_files)

def test_zip_files(download_pdf, download_csv):
    with zipfile.ZipFile('..\\resources\\myZip.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        for files in file_dir:
            add_files = os.path.join(path_files, files)
            my_zip.write(add_files, basename(add_files))


def test_add_zip_file(download_xlsx):
    with zipfile.ZipFile('..\\resources\\myZip.zip', mode='a', compression=zipfile.ZIP_DEFLATED) as add_zip:
        add_zip.write(path_xlsx, basename(path_xlsx))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    create_sours = os.path.abspath(os.path.join(current_dir, '..', 'resources'))

def test1():
    print(path_files)
