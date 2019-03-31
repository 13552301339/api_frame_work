import requests
from common.api_logging import MyLog


api_logger = MyLog()

# 封装接口请求
class HttpRequest(object):

    def http_request(self, url, param, http_method, cookies):

        if http_method == "GET":
            try:
                res = requests.get(url, param, cookies=cookies)
                # api_logger.info('')
            except Exception as e:
                # api_logger.error("")
                print(e)

        else:
            try:
                res = requests.post(url, param, cookies=cookies)
                # api_logger.info('')
            except Exception as e:
                # api_logger.error("")
                print(e)

        # print(res.json())
        return res


if __name__ == '__main__':
    url = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"

    param = {'mobilephone': '123', 'pwd': '123456'}

    res = HttpRequest().http_request(url, param, "POST", None)
    print(res.json())

