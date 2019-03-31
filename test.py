from api_frame_work.common.read_config import ReadConfig
from api_frame_work.common import file_path
res = eval(ReadConfig().read_config(file_path.config_path, 'CASECONFIG', 'sheet_dict'))

print(type(res))

a = [1,2,3,4]
a.re