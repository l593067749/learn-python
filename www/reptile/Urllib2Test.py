# -*- coding: UTF-8 -*-
import urllib2
import urllib
import cookielib
class Urllib2Test(object):


    def getUrl(self,url):
        try:
            user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
            headers = { 'User-Agent' : user_agent }
            request=urllib2.Request(url,headers=headers)
            #其他方法 request.get_method=lambda :'PUT' # or 'DELETE'
            response=urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError,e:
                print e.code
        return None

    def postUrl(url,data={}):
        request=urllib2.Request(url)
        data=urllib.urlencode(data)
        response=urllib2.urlopen(request,data)
        return response.read()
        print getUrl("http://cuiqingcai.com/954.html")
        print "----------------------------post--------------------------------------------------"
        #print postUrl("http://www.baidu.com")

    # cookie 使用

    def cookieSiample(self):
        #创建MozillaCookieJar实例对象
        cookie = cookielib.MozillaCookieJar()
        #从文件中读取cookie内容到变量
        cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
        #创建请求的request
        req = urllib2.Request("http://www.baidu.com")
        #利用urllib2的build_opener方法创建一个opener
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        response = opener.open(req)
        print response.read()
        for item in cookie:
            print 'Name = '+item.name
            print 'Value = '+item.value

    def saveCookieFile(self):
        #设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie.txt'
        #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        handler = urllib2.HTTPCookieProcess or(cookie)
        #通过handler来构建opener
        opener = urllib2.build_opener(handler)
        #创建一个请求，原理同urllib2的urlopen
        response = opener.open("http://www.baidu.com")
        #保存cookie到文件
        cookie.save(ignore_discard=True, ignore_expires=True)

#saveCookieFile()
#cookieSiample()

