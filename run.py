import unittest
from common.test_api import TestApi
import HTMLTestRunnerNew
from common import file_path
import datetime
nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 加载测试用例
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestApi))

with open(file_path.repore_path, 'wb') as file:
    # 测试报告
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='报告', description=nowTime, tester='chaox')

    runner.run(suite)

