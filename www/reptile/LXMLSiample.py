# -*- coding: UTF-8 -*-
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item2</a>
     </ul>
 </div>
'''

def number01():
    html = etree.HTML(text)
    result = etree.tostring(html)
    print(result)

def no02():
    html = etree.HTML(text)
    result = html.xpath('//li[@class="item-0"]/a')
    for r in result:
        print r.text
        print r.xpath('./@href')

no02()