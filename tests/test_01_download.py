import os.path
from time import sleep

import requests

'''Создание webdriver с кастомными настройками: изменение пути для скачиваемых файлов в браузере.
Без них файл скачивается в дирректорию по умолчанию (Например, в папку Загрузки).
Необходимы, если файл скачивается не по прямой ссылке, а при использовании действий в браузере (например, нужно нажать кнопку Загрузить)'''

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

current_dir = os.path.dirname(__file__)
download_sours = os.path.abspath(os.path.join(current_dir, '..', 'resources'))

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_sours, #'C:\\Users\\Hanna\\PycharmProjects\\qa_guru_python_4_7\\resources',
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

browser.config.driver = driver

'''Настройки для скачивания напрямую с web. Файлы сохраняются в проект в папку с файлом теста'''

url_pdf = "https://bugs.python.org/file47781/Tutorial_EDIT.pdf"
url_xlsx = "https://go.microsoft.com/fwlink/?LinkID=521962"
url_csv = "https://support.staffbase.com/hc/en-us/articles/360007108391-CSV-File-Examples"

response_pdf = requests.get(url_pdf, allow_redirects=True)
response_xlsx = requests.get(url_xlsx, allow_redirects=True)
response_csv = requests.get(url_csv, allow_redirects=True)


def test_download_pdf():
    with open('..\\resources\\dummy.pdf', 'wb') as file_pdf:
        file_pdf.write(response_pdf.content)


def test_download_xlsx():
    with open('Financial Sample.xlsx', 'wb') as file_xlsx:
        file_xlsx.write(response_xlsx.content)


def test_download_csv():
    browser.open(url_csv)
    browser.element('//a[contains(text(),"Data Set for Username Onboarding")]').click()
    sleep(5)
    print(os.path.abspath(__file__))

# def test_remove_files():
#     remove_pdf = os.remove('..\\resources\\dummy.pdf')
