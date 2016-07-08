#coding:utf-8

import xml.dom.minidom as domlib
import re


topHostPostfix = (
    '.com', '.la', '.io', '.co', '.info', '.net', '.org', '.me', '.mobi',
    '.us', '.biz', '.xxx', '.ca', '.co.jp', '.com.cn', '.net.cn',
    '.org.cn', '.mx', '.tv', '.ws', '.ag', '.com.ag', '.net.ag',
    '.org.ag', '.am', '.asia', '.at', '.be', '.com.br', '.net.br',
    '.bz', '.com.bz', '.net.bz', '.cc', '.com.co', '.net.co',
    '.nom.co', '.de', '.es', '.com.es', '.nom.es', '.org.es',
    '.eu', '.fm', '.fr', '.gs', '.in', '.co.in', '.firm.in', '.gen.in',
    '.ind.in', '.net.in', '.org.in', '.it', '.jobs', '.jp', '.ms',
    '.com.mx', '.nl', '.nu', '.co.nz', '.net.nz', '.org.nz',
    '.se', '.tc', '.tk', '.tw', '.com.tw', '.idv.tw', '.org.tw',
    '.hk', '.co.uk', '.me.uk', '.org.uk', '.vg', ".com.hk")
regx = r'[^\.]+(' + '|'.join([h.replace('.', r'\.') for h in topHostPostfix]) + ')$'
pattern = re.compile(regx, re.IGNORECASE)


class Mydblib:
    filename = "test.xml"
    def __init__(self):
        try:
            self.dom = domlib.parse(self.filename)
            self.root = self.dom.documentElement
        except:
            try:
                impl = domlib.getDOMImplementation()
                self.dom = impl.createDocument(0,"bookmarks",0)
                self.root = self.dom.documentElement
            except:
                print "数据文件初始化失败"

    def save(self):
        f = open(self.filename,"w")
        self.dom.writexml(f)
        f.close()

    def addbookmark(self,title,url):
        booknodes = self.dom.getElementsByTagName("bookmark")
        tarbooknode = 0
        for booknode in booknodes:
            atr = booknode.getAttribute('title')
            if(atr == title):
                tarbooknode = booknode
                break
        if(tarbooknode == 0):
            tarbooknode = self.dom.createElement("bookmark")
            tarbooknode.setAttribute("title",title)
            self.root.appendChild(tarbooknode)
        tarbooknode.setAttribute("url",url)
if __name__ == "__main__":
    db = Mydblib()
    db.addbookmark()
    db.save()
