import os
from selenium import webdriver

chrome = webdriver.Chrome(executable_path="D:\Mars\QA\OTUS\lesson_10\WebDrivers\chromedriver")
# chrome = webdriver.Chrome(executable_path=os.path.expanduser("~\OTUS\lesson_10\WebDrivers\chromedriver"))

chrome.close()
print()
