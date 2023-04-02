import os
import zipfile
from os.path import basename

# current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.dirname(__file__)
# path_csv = os.path.join(current_dir, '..', 'resources', 'username.csv')
path_xlsx = os.path.abspath('Financial Sample.xlsx')
# path_pdf = os.path.abspath(current_dir, '..', 'dummy.pdf')

path_files = os.path.join(current_dir, '..', 'resources')
file_dir = os.listdir(path_files)


# with zipfile.ZipFile('myZip.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write(path_csv, basename(path_csv))

with zipfile.ZipFile('..\\resources\\myZip.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    for files in file_dir:
        add_files = os.path.join(path_files, files)
        my_zip.write(add_files, basename(add_files))

with zipfile.ZipFile('..\\resources\\myZip.zip', mode='a', compression=zipfile.ZIP_DEFLATED) as add_zip:
    add_zip.write(path_xlsx, basename(path_xlsx))
    # add_zip.write(path_pdf, basename(path_pdf))

# path_pdf = 'C:\\Users\\Hanna\\PycharmProjects\\qa_guru_python_4_7\\tests'
# pdf_file_dir = os.listdir(path_pdf)
#
# path_xlsx = 'C:\\Users\\Hanna\\PycharmProjects\\qa_guru_python_4_7\\tests\\..xlsx'
# xlsx_file_dir = os.listdir(path_xlsx)
#
# with zipfile.ZipFile('myZip.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as add_to_zip:
#     # add_to_zip.write(pdf_file_dir, filename='../resources/dummy(1).pdf')
#     # for file_xlsx in xlsx_file_dir:
#         add_xlsx = os.path.join(path_xlsx)
#         add_to_zip.write(add_xlsx)


current_dir = os.path.dirname(os.path.abspath(__file__))
create_sours = os.path.abspath(os.path.join(current_dir, '..', 'resources'))

