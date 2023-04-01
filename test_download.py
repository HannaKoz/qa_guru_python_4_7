import requests

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": '/Users/Hanna/PycharmProjects/qa_guru_python_4_7/resources',
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
 driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

browser.config.driver = driver


url_pdf = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
url_xlsx = "https://go.microsoft.com/fwlink/?LinkID=521962"
url_csv = "https://support.staffbase.com/hc/en-us/articles/360007108391-CSV-File-Examples"


def test_download_pdf():
    browser.open_url(url_pdf)
    response_pdf = requests.get(url_pdf, allow_redirects=True)
    with open("dummy.pdf", "wb") as file_pdf:
        file_pdf.write(response_pdf.content)
    # assert file_pdf is "dummy.pdf"


# def download_xlsx():
#     pass
#
# def download_csv():
#     pass
#
# def zip_files():
#     pass
#
# def add_zip_to_folder():
#     pass
#
# def check_pdf_in_zip():
#     pass
#
# def check_xlsx_in_zip():
#     pass
#
# def check_csv_in_zip():
#     pass