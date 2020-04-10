# coding=utf-8
import configparser


class Config(object):

    def __init__(self, route, name=None):
        # route: 文件及路径名
        self.route = route
        self.name = name

    def get_config(self, key):
        """
        可以读取配置信息
        :param name:数据名称
        :param key:主键
        :return:值
        """
        try:
            cf = configparser.ConfigParser()
            cf.read(self.route, encoding='utf-8')
            # 取指定值
            value = cf.get(self.name, key)
        except Exception as e:
            raise e
        return value

    def split_txt(self, key):
        a = self.get_config(key)
        a = a.split('|')
        return a


if __name__ == '__main__':
    cf = Config(r'..\DataLayer\ShopElementData.ini', '商品分类')
    user_name1, user_name2 = cf.split_txt('分类_厨具')
    print(user_name1, user_name2)