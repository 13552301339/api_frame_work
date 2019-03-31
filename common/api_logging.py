# 日志级别  debug, info, warning, error, critical
import logging
from common import file_path


class MyLog(object):

    def my_log(self, level, msg):
        # 日志收集器
        my_logger = logging.getLogger('api_frame_work')
        my_logger.setLevel("DEBUG")

        # 格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        # 输出控制台通道
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)
        my_logger.addHandler(ch)

        # 输出到文件
        fh = logging.FileHandler(file_path.log_path, encoding='utf-8')
        fh.setFormatter(formatter)

        # 给日志收集器添加渠道
        my_logger.addHandler(fh)
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)

if __name__ == '__main__':

    my_logger = MyLog()

    my_logger.my_log('DEBUG', '你猜')

