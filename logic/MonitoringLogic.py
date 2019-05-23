# coding: utf-8

import logger
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.select import Select

class MonitoringException(Exception):
    def __init__(self, message):
        super().__init__(message)


class MonitoringLogic:
    def __init__(self):
        self.logger = logger.logger('MonitoringLogic')

    def Monitoring(self):
        options = ChromeOptions()
        options.add_argument('--headless')  # 画面を表示せずに動作させることが可能
        driver = Chrome(executable_path='.\\bin\\chromedriver.exe', options=options)

        url = ''


if __name__ == '__main__':
    logic = MonitoringLogic()
    logic.Monitoring()
