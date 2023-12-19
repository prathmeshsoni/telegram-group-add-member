import time

from config import *
from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        dir_path = fr"C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 0"
        browser = p.chromium.launch_persistent_context(
            channel="chrome",
            user_data_dir=dir_path,
            headless=False,
            args=["--incognito"]
        )
        website = f'https://web.telegram.org/k/'
        pages = browser.pages
        default_page = pages[0]
        default_page.goto(website, timeout=60000)
        time.sleep(5)

        try:
            default_page.locator('//div[@class="input-search"]/input').type('', timeout=120000)
        except:
            pass
        try:
            input('Please Scan QR Code')
            default_page.screenshot(path='demo.png', full_page=True)
        except:
            pass
        time.sleep(0.5)
        try:
            default_page.click('(//div[@class="search-group search-group-contacts"]//ul[@class="chatlist"])[1]/a')
        except:
            pass
        time.sleep(0.5)
        try:
            default_page.click('//div[@class="chat-info"]')
        except:
            pass

        time.sleep(0.5)

        try:
            default_page.click("(//span[contains(text(), 'Members')])[2]/../..")
        except:
            pass
        time.sleep(0.5)

        username_list = []
        member_list = default_page.locator(
            '//div[@id="column-right"]//div[@class="search-super-tabs-container tabs-container"]//ul[@class="chatlist"]/a').element_handles()

        for i in member_list:
            try:
                i.click()
            except:
                pass
            time.sleep(0.5)
            try:
                username = default_page.locator(
                    "//div[@class='row row-with-icon row-with-padding row-clickable hover-effect rp']//*[contains(text(), 'Username')]/../following-sibling::div").inner_text()
            except:
                username = ''
            if not username:
                try:
                    default_page.locator(
                        '//div[@class="chat tabs-tab active"]//div[@class="new-message-wrapper rows-wrapper-row"]//div[@class="input-message-container"]/div[@class="input-message-input is-empty i18n scrollable scrollable-y no-scrollbar"]').type(
                        "hey")
                except:
                    pass
                time.sleep(1)
                try:
                    default_page.click('//button[@class="btn-icon rp btn-circle btn-send animated-button-icon send"]')
                except:
                    pass
                time.sleep(0.5)
                try:
                    username = default_page.locator(
                        '//div[@class="chat tabs-tab active"]//span[@class="peer-title"] | //div[@class="chat tabs-tab active"]//span[@class="peer-title-inner"]').inner_text()
                except:
                    username = ''
            try:
                default_page.click(
                    '//div[@class="chat tabs-tab active"]//div[@class="chat-info-container"]/button[@class="btn-icon sidebar-close-button"]')
            except:
                pass
            print(f'username = {username}')
            if username:
                username_list.append(username)
            time.sleep(0.5)

        try:
            default_page.locator('//div[@class="input-search"]/input').type(f"{add_group}")
        except:
            pass

        time.sleep(0.5)
        try:
            default_page.click('(//div[@class="search-group search-group-contacts"]//ul[@class="chatlist"])[1]/a')

        except:
            pass
        time.sleep(0.5)
        try:
            default_page.click('//div[@class="chat-info"]')
        except:
            pass
        time.sleep(0.5)

        for user in username_list:
            try:
                default_page.click(
                    '//div[@id="column-right"]//div[@class="sidebar-content"]//button[@class="btn-circle btn-corner z-depth-1 rp"]')
            except:
                pass
            time.sleep(0.5)
            try:
                default_page.locator('//div[@class="popup-title"]/input').type(user)
            except:
                pass
            time.sleep(1)
            try:
                default_page.click('(//div[@class="popup popup-forward active"]//ul[@class="chatlist"]/a)[1]')
            except:
                pass
            time.sleep(0.5)
            try:
                default_page.click('//*[contains(text(), "Add")]/parent::button[@class="btn primary rp"]')
            except:
                pass
            time.sleep(0.5)

        browser.close()


if __name__ == '__main__':
    main()
