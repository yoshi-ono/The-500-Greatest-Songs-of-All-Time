from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

service = ChromeService(executable_path="/opt/WebDriver/bin/chromedriver")
#options = ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

print(driver.title)
# => "Google"

fw = open("page_source.html", "w")
fw.write(driver.page_source)
fw.close()

fw = open("soup_prettify.html", "w")
soup = BeautifulSoup(driver.page_source, "html.parser")
fw.write(soup.prettify())
fw.close()

driver.implicitly_wait(0.5)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

search_box.send_keys("Selenium")
search_button.click()

print(driver.find_element(By.NAME, "q").get_attribute("value"))
# => "Selenium"

driver.quit()
