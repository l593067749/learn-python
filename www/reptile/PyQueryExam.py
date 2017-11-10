# -*- coding: UTF-8 -*-
from pyquery import PyQuery as pq
from lxml import etree

'解析html，跟jquery语法相似'

html='''<div>
    <ul>
         <li class="item-0">第一个</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>'''
#先补全html
#html=etree.HTML(html)
#print etree.tostring(html)
print type(html)
doc=pq(html.decode("utf-8"))
lis=doc('li[class="item-0"]')
for li in lis.items():
    print type(li.html())
    print li.html()



