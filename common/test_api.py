import unittest
from common.do_excel import DoExcel
from common.http_requist import HttpRequest
from ddt import ddt, data
from common import file_path
from common.api_logging import MyLog
# 主要记录登录状态
COOKIES = None
# 获取配置信息
# button = ReadConfig().read_config(file_path.config_path, 'FLAG', 'button')
# sheet_list = eval(ReadConfig().read_config(file_path.config_path, 'CASECONFIG', 'sheet_list'))

# 获取测试用例
test_data = DoExcel(file_path.testcase_path).get_data()
api_logger = MyLog()

@ddt
class TestApi(unittest.TestCase):

    def setUp(self):
        api_logger.info('开始测试')

    @data(*test_data)
    def test_api(self, data_item):
        global COOKIES

        api_logger.info('正在运行第%d条用例：%s' % (data_item['id'], data_item['description']))
        api_logger.info('测试数据是:%s' % data_item['param'])

        res = HttpRequest().http_request(data_item['url'], eval(data_item['param']), data_item['http_method'], COOKIES)
        # 判断上一个请求有没有COOKIES
        if res.cookies:
            COOKIES = res.cookies
        api_logger.info('测试结果是：%s' % res)

        try:
            self.assertEqual(str(data_item['ExpectedResult']), res.json()['code'])
            test_result = 'PASS'

        except AssertionError as e:
            test_result = 'FAIL'
            api_logger.error('请求出错了，错误是：%s' % e)
            raise e
        finally:
            # 测试结果写回
            DoExcel(file_path.testcase_path).weite_back(data_item['module'], data_item['id']+1, res.json()['code'], test_result)
        # print(res)

    def tearDown(self):

        # DoExcel().weite_back('../test_data/api.xlsx', 'testcase', )
        api_logger.info('结束这个测试')


