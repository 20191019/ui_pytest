import pymysql

def mysql(sql):
    """
    mysql数据库方法
    :param sql:sql语句 str
    :return: 执行结果（tuple）
    """
    # 连接数据库
    db = pymysql.connect("120.24.78.4", "root", "kbs0755", "tf-ism")
    # 获取游标
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交数据库
        db.commit()
    except Exception as err:
        print(err)
        # 发生错误回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
    # 返回结果
    list_var = cursor.fetchall()
    return list_var