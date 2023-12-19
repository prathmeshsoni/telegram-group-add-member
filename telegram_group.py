from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from config import *

options = Options()

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://web.telegram.org/k/")
time.sleep(10)
try:
    input('Please Scan QR Code')
except:
    pass
time.sleep(2)
try:
    driver.find_element(by=By.XPATH, value='//div[@class="input-search"]/input').send_keys(f"{search_group}")
except:
    pass
time.sleep(0.5)
try:
    driver.find_element(by=By.XPATH, value='(//div[@class="search-group search-group-contacts"]//ul[@class="chatlist"])[1]/a').click()
except:
    pass
time.sleep(0.5)
try:
    driver.find_element(by=By.XPATH, value='//div[@class="chat-info"]').click()
except:
    pass

time.sleep(0.5)

try:
    driver.find_element(by=By.XPATH, value="(//span[contains(text(), 'Members')])[2]/../..").click()
except:
    pass
time.sleep(0.5)

driver.find_elements(by=By.XPATH, value='//div[@class="search-super-tabs-container tabs-container"]//ul[@class="chatlist"]/a')
# print('test')
username_list = []
member_list = driver.find_elements(by=By.XPATH,
                                   value='//div[@id="column-right"]//div[@class="search-super-tabs-container tabs-container"]//ul[@class="chatlist"]/a')
for i in member_list[1:]:
    try:
        i.click()
    except:
        pass
    time.sleep(0.5)
    try:
        username = driver.find_element(by=By.XPATH,
                                       value="//div[@class='row row-with-icon row-with-padding row-clickable hover-effect rp']//*[contains(text(), 'Username')]/../following-sibling::div").text
    except:
        username = ''
    if not username:
        try:
            driver.find_element(by=By.XPATH, value='//div[@class="new-message-wrapper rows-wrapper-row"]//div[@class="input-message-container"]/div[@class="input-message-input is-empty i18n scrollable scrollable-y no-scrollbar"]').send_keys("hey")
        except:
            pass
        time.sleep(1)
        try:
            driver.find_element(by=By.XPATH, value='//button[@class="btn-icon rp btn-circle btn-send animated-button-icon send"]').click()
        except:
            pass
        time.sleep(0.5)
        username = driver.find_element(by=By.XPATH, value='//div[@class="chat tabs-tab active"]//span[@class="peer-title"] | //div[@class="chat tabs-tab active"]//span[@class="peer-title-inner"]').text
    try:
        driver.find_element(by=By.XPATH,
                            value='//div[@class="chat tabs-tab active"]//div[@class="chat-info-container"]/button[@class="btn-icon sidebar-close-button"]').click()
    except:
        pass
    print(f'username = {username}')
    username_list.append(username)
    time.sleep(0.5)

try:
    driver.find_element(by=By.XPATH, value='//div[@class="input-search"]/input').send_keys(f"{add_group}")
except:
    pass

time.sleep(0.5)
try:
    driver.find_element(by=By.XPATH,
                        value='(//div[@class="search-group search-group-contacts"]//ul[@class="chatlist"])[1]/a').click()
except:
    pass
time.sleep(0.5)
try:
    driver.find_element(by=By.XPATH, value='//div[@class="chat-info"]').click()
except:
    pass
time.sleep(0.5)


for user in username_list:
    try:
        driver.find_element(by=By.XPATH, value='//div[@id="column-right"]//div[@class="sidebar-content"]//button[@class="btn-circle btn-corner z-depth-1 rp"]').click()
    except:
        pass
    time.sleep(0.5)
    try:
        driver.find_element(by=By.XPATH, value='//div[@class="popup-title"]/input').send_keys(user)
    except:
        pass
    time.sleep(1)
    try:
        driver.find_element(by=By.XPATH, value='(//div[@class="popup popup-forward active"]//ul[@class="chatlist"]/a)[1]').click()
    except:
        pass
    time.sleep(0.5)
    try:
        driver.find_element(by=By.XPATH, value='//*[contains(text(), "Add")]/parent::button[@class="btn primary rp"]').click()
    except:
        pass
    time.sleep(0.5)


driver.quit()
