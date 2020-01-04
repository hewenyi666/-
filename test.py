if __name__ == '__main__':
    s = "username=Will&password=123456"
    dic = {}
    res = s.split("&")
    print(res)
    for i in res:
        tmp = i.split("=")
        dic[tmp[0]] = tmp[1]
    print(dic)