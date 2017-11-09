# -*- coding: UTF-8 -*-
'错误相关'

import logging
logging.basicConfig(filename="../../log/example.log",level=logging.INFO)


class MyError(StandardError):
    pass

def tryTest(num):
    try:
        logging.info( 'try ...')
        r=division(num)
        logging.info( 'result:%d',r)
    except ZeroDivisionError,e:
        logging.exception(e)
    else:
        logging.info( 'no info')
    finally:
        logging.info( 'finally...')
    logging.info( 'END')

def division(num):
    return 10/num

def testMyError():
    raise MyError("this is my Error") #抛出错误


tryTest(2);
logging.info( "---------------tryTest(0)-------------")
tryTest(0);
logging.info( "--------------testMyError---------------")
testMyError()
logging.info( "-----------------division(0)-------------")
division(0);