# -*- coding: UTF-8 -*-

import requests
class RequestsTest(object):
    def getUrl(self,url,params={},headers={},cookies={}):
        r=requests.get(url,params=params,headers=headers,cookies=cookies)
        #r.encoding="utf-8"
        #print r.status_code
        #print r.encoding
        #print r.cookies
        #print r.text
        return r


    def postUrl(self,url,params={},headers={},files={},cookies={}):
        r = requests.post(url, data=params,files=files)
        return r

    # 两次请求一个会话
    def sessionManage(self):
        s = requests.Session()
        s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
        r = s.get("http://httpbin.org/cookies")
        print r.text

    def test(self):
        reqTest=RequestsTest()

        reqTest.sessionManage()
        # http://httpbin.org 是一个公共的测试网址
        reqTest.getUrl("http://www.baidu.com")
        # post test
        params = {'key1': 'value1', 'key2': 'value2'}
        files  ={'file': open('../../log/test.log', 'rb')}
        postR=reqTest.postUrl("http://httpbin.org/post",params=params,files=files)
        print postR.text

