import time

from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage

driver = webdriver.Chrome("D:/Work/Intetics/Python_course/chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://www.instagram.com/accounts/login/")
login_page = LoginPage(driver)
login_page.enter_username("pyautomation")
login_page.enter_password("Ab123456789!")
login_page.click_login()

main_page = MainPage(driver)
main_page.click_not_now_button()
main_page.type_in_search_field("#fitness")
main_page.click_result_with_text("#fitness")

search_results_page = SearchResultsPage(driver)
time.sleep(5)
assert "Подписаться" in search_results_page.get_follow_button_text()
driver.quit()
