# 配置文件 ini conf config properties

from common import file_path

# 读取都是字符串类型

from configparser import ConfigParser

# 封装配置文件读取
class ReadConfig(object):

    def read_config(self, file_path, section, option):
        cf = ConfigParser()

        cf.read(file_path, encoding='utf-8')

        res = cf.get(section, option)
        return res


if __name__ == '__main__':
    button = ReadConfig().read_config(file_path.config_path, 'FLAG',
                                      'button')
    res = eval(button)
    print()
