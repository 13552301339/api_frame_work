import os
import datetime
nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
# 等同../
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)

# 配置文件
config_path = os.path.join(project_path, 'config', 'case.config')
# print(config_path)

#测试用例

testcase_path = os.path.join(project_path, 'test_data', 'api.xlsx')

# 测试报告

repore_path = os.path.join(project_path, 'test_result', 'report', 'test_api.html')

# 日志  根据时间每天一个文件

log_path = os.path.join(project_path, 'test_result', 'logs', 'api_frame_work_'+str(nowTime)+'.txt')

# print(project_path)

# 数据库配置文件路径

db_config_path = os.path.join(project_path, 'config', 'db.config')




