# coding=utf-8
import configparser


class Config(object):

    def __init__(self, route):
        # route: 文件及路径名
        self.route = route

    def get_config(self, name, key):
        """
        可以读取配置信息
        :param name:数据名称
        :param key:主键
        :return:值
        """
        cf = configparser.ConfigParser()
        cf.read(self.route)
        # 取指定值
        value = cf.get(name, key)
        return value


if __name__ == '__main__':
    cf = Config(r'D:\py\ui_pytest\ToConfigure\case.ini')
    user_name = cf.get_config('test_login_001', 'dd')
    print(user_name)
