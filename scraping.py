from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

service = ChromeService(executable_path="/opt/WebDriver/bin/chromedriver")
#options = ChromeOptions()
driver = webdriver.Chrome(service=service)

#driver.get("https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/")
driver.get("https://www.rollingstone.com/music/music-lists/500-greatest-songs-of-all-time-151127/")

filename = driver.title.replace(" ", "_") + ".md"
print(filename)

# fw = open("page_source.html", "w")
# fw.write(driver.page_source)
# fw.close()

fw = open("soup_prettify.html", "w")
soup = BeautifulSoup(driver.page_source, "html.parser")
fw.write(soup.prettify())
fw.close()

driver.implicitly_wait(0.5)

nav_bar = driver.find_element(By.ID, "pmc-gallery-list-nav-bar-render")
a_list = nav_bar.find_elements(By.TAG_NAME, "a")

urls = []

for anker in a_list:
    text = anker.text
    href = anker.get_attribute('href')
    print(text, href)
    urls.append(href)

fw = open(filename, "w")

for url in urls:
    driver.get(url)

    element = driver.find_element(By.CLASS_NAME, "c-gallery-vertical-album__title")
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()

    pmc = driver.execute_script('return pmcGalleryExports')

    for song in pmc['gallery']:
        position = song['positionDisplay']
        title = "**" + song['title'].replace(", '", "**, '")
        line = f"{position}, {title}"
        fw.write(line + '  \n')

fw.close()

driver.quit()
