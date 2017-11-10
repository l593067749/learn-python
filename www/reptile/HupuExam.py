# -*- coding: UTF-8 -*-
import threading
import urllib
from pyquery import PyQuery as pq
from lxml import etree
import os
import time
from RequestsTest import RequestsTest

def no01():
    request=RequestsTest()
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    headers = { 'User-Agent' : user_agent }
    response=request.getUrl("https://bbs.hupu.com/bxj")
    print response.encoding
    html=etree.HTML(response.content)
    #html=response.text
    doc=pq(etree.tostring(html).decode("UTF-8"))
    lis=doc('ul[class="for-list"] li')
    for li in lis.items():
        title=li('div[class="titlelink box"] a')
        author=li('div[class="author box"] a').text()
        ansour=li('span[class="ansour box"]').text()
        print "[%s-https://bbs.hupu.com%s]-[%s]-[%s]" % (title.text(),title.attr("href"),author,ansour)
        print "---------------------------------------------------"
def randomString(n):
    return (''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(n))))[0:16]
def no02():
    url="https://bbs.hupu.com/20688151.html";
    html=pq(url=url,encoding="UTF-8")
    title=html('div[class="subhead"] span').html()
    print title
    no=html('img')
    for temp in no.items():
        print temp.outer_html()
        downFile(temp.attr("src"))
        print "-----------------------"

def thradeDown():
    url="https://bbs.hupu.com/20688151.html";
    html=pq(url=url,encoding="UTF-8")
    title=html('div[class="subhead"] span').html()
    print title
    no=html('img')
    for temp in no.items():
        print temp.outer_html()
        t=threading.Thread(target=downFile,args=(temp.attr("src"),))
        t.start()
        t.join()
        print t.name

def downFile(img_url):
    try:
        if(str.startswith(img_url,"//")):
            img_url="http:"+img_url
        if(len(img_url.split("?"))>1):
            img_url=img_url.split("?")[0]
        filePath=os.path.abspath('./../../log')
        file_suffix = os.path.splitext(img_url)[-1]
        filename='{}{}{}{}'.format(filePath,os.sep,randomString(16),file_suffix)
        urllib.urlretrieve(img_url,filename=filename)
    except StandardError,e:
            print  img_url
            e.message

def delFile():
    rootDir=os.path.abspath('./../../log')
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        file_suffix = os.path.splitext(path)[-1]
        print "%s---%s" % (path,file_suffix)
        if(file_suffix==".log"):
            pass
        else:
            os.remove(path)



    #no02()

delFile()
t1=time.time()
thradeDown()
#no02()
t2=time.time()
print t2-t1