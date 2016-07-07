# -*- coding: utf-8 -*-
import xml.dom.minidom as mydom
import os
import codecs

print os.getcwd()


def addbookmark(url,title,filename):
    dom = mydom.parse(filename)
    tembook = dom.createElement("bookmark")
    tembook.setAttribute("url",url)
    text = dom.createTextNode(title)
    tembook.appendChild(text)
    content = dom.getElementsByTagName("content")
    content[0].appendChild(tembook)
    f=file(filename, 'w')
    dom.writexml(f)
    f.close()
