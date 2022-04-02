# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 10:32
# @Author  : Caokun
# @FileName: driver.py
# @Software: PyCharm

from selenium import webdriver


class GetDriver():

    # 获取 driver
    def get_driver(self):
        options = webdriver.ChromeOptions()

        options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("disable-blink-features=AutomationControlled")  # chrome去掉了webdriver痕迹
        options.add_argument("--disable-blink-features")

        args = ["hide_console", ]
        self.browser = webdriver.Chrome(chrome_options=options,service_args=args)

        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                            Object.defineProperty(navigator, 'webdriver', {
                              get: () => undefined
                            })
                          """
        })

        self.browser.maximize_window()
        # 返回 driver
        global browser
        browser = self.browser

        return self.browser

    def take_over_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.browser = webdriver.Chrome(chrome_options=options)

        options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("disable-blink-features=AutomationControlled")  # chrome去掉了webdriver痕迹
        options.add_argument("--disable-blink-features")

        # self.browser = webdriver.Chrome(chrome_options=options)

        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                            Object.defineProperty(navigator, 'webdriver', {
                              get: () => undefined
                            })
                          """
        })

        self.browser.maximize_window()
        global browser
        browser = self.browser
        # 返回 driver
        return self.browser

    # 关闭driver
    def quit_driver(self):
        browser.quit()


if __name__ == '__main__':
    GetDriver().quit_driver()