# _*_ coding: utf-8 _*_
import codecs
import os
import shutil
import time
def readFile(filePath):
    with open(filePath,'r') as f:
            print f.read()

def readFile2(filePath):
    with codecs.open(filePath,'r','utf-8') as f:#指定编码
        for line in f.readlines():
            print(line.strip())

def readFile3(filePath):
    with open(filePath,'r') as f:
        for line in f:
            print(line.strip())

def readFile4(filePath):
    with open(filePath,'r') as f: #适合读二进制文件
            while True:
                    lines=f.read(50)
                    if not lines:
                        break
                    print lines

def writeFile(filePath):
    with codecs.open(filePath,'w','utf-8') as f:#指定编码
        f.write(u'皮皮虾我们走')

filePath=os.path.abspath('./../../log')

readFile(filePath+"/example.log")#读
writeFile(filePath+"/test.log")#写

testBakPath=filePath+"/"+time.strftime("%Y-%m-%d", time.localtime())+"-testBak.log"
if(os.path.isfile(testBakPath)==False):#复制文件
    shutil.copyfile(filePath+"/test.log",testBakPath)

