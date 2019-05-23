# coding: utf-8
import logger
from logic.MonitoringLogic import MonitoringLogic
from logic.MonitoringLogic import MonitoringException
from logic.NotificationLogic import NotificationLogic
from logic.NotificationLogic import NotificationException


class Main:
    def __init__(self):
        pass

    def main(self):
        # 1.スクレイピングする処理を実行
        hoge = MonitoringLogic.Monitoring()

        # 2.LINEAPIを実行して通知する処理
        fuga = NotificationLogic.Notification()


if __name__ == '__main__':
    main = Main()
    main.main()
