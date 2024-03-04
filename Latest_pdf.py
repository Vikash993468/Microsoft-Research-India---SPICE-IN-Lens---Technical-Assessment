from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()

options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.ncbi.nlm.nih.gov/pmc/")
driver.maximize_window()
# driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "Journal List").click()
driver.find_element(By.LINK_TEXT, "AACE Clinical Case Reports").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .va_middle .arc-issue").click()
driver.find_element(By.LINK_TEXT, "PDF–198K").click()
driver.implicitly_wait(10)

driver.close()
