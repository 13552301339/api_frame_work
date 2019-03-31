import mysql.connector
from common.read_config import ReadConfig
from common import file_path

class DoMysql(object):
    def do_mysql(self, sql):
        # 数据库连接信息
        config = eval(ReadConfig().read_config(file_path.db_config_path, 'DB', 'config'))

        # 产生数据库连接
        conn = mysql.connector.connect(**config)

        # 获取数据库操作权限

        cursor = conn.cursor()

        # sql = 'select * form coupon'

        # 执行
        cursor.execute(sql)

        # 获取数据

        res = cursor.fetchall()

        # 关闭
        cursor.close()

        conn.close()
        return res

