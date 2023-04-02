from zipfile import ZipFile


def test_check_pdf():
    with ZipFile('..\\tests\\myZip.zip') as zip_:
        print(zip_.namelist())