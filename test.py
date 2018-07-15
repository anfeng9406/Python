# from urllib import request
#
# import chardet
#
# if __name__ == '__main__':
#     response = request.urlopen("http://fanyi.baidu.com")
#     html = response.read()
#     #html = html.decode('utf-8')
#     charset = chardet.detect(html)
#     print(charset)


from urllib import request


if __name__ == '__main__':
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    print(html)