# coding: utf-8

import logger


class NotificationException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NotificationLogic:
    def __init__(self):
        self.logger = logger.logger('MonitoringLogic')

    def Notification(self):
        # Todo: LINE APIを使用して通知する処理を追加する
        pass


if __name__ == '__main__':
    logic = NotificationLogic()
    logic.Notification()
