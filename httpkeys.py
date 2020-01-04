import requests
import json


class HTTP:
    def __init__(self):
        self.session = requests.session()
        self.url = ""
        self.params = {}
        self.result = None
        self.jsonres = None  # 转为json格式的结果
        self.pick = None

    def seturl(self, u):
        self.url = u + "/"
    def addheader(self,key,value): # 添加请求头
        value = self.get_value(value)  # 如果是{token}形式,则提取token';直接是token,则不影响
        self.session.headers[key] = value

    def removerheader(self, key):
        try:
            self.session.headers.pop(key)
        except Exception as e:
            print(e)

    def post(self, url, params):
        now_url = self.url + url
        self.result = self.session.post(now_url, data=self.get_params(params))
        return self.result

    def savajson(self,key):  # 保存获取的token(json中的值)
        self.jsonres = json.loads(self.result)
        return self.jsonres[key]

    def get_params(self):  # 输入的值是"45343nv&asdf" 格式的,转换为字典格式
        self.params.clear()
        dic = {}
        res = self.params.split("&")
        for i in res:
            tmp = i.split("=")
            dic[tmp[0]] = tmp[1]
        return dic

    def assertequals(self, key, value):
        # 校验json结果,键和值是否一致
        if str(self.jsonres[key]) == value:
            print("Pass")
        else:
            print("Fail")
    def get_value(self,p):  # 从{token}中取出token
        for key in self.jsonres.keys():
            p = p.replace("{" + key + "}",self.jsonres[key])
        return p