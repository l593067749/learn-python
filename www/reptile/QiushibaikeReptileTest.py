# -*- coding: UTF-8 -*-
from Urllib2Test import Urllib2Test
class QiushibaikeReptileTest(object):
    def number01(self):
        urllib2Test=Urllib2Test()
        response= urllib2Test.getUrl("http://www.qiushibaike.com/hot/page/1")
        print response


qRTest=QiushibaikeReptileTest()
qRTest.number01()