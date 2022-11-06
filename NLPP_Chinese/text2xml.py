from xml.dom.minidom import parse
import os, xml.dom.minidom
from xml.etree.ElementTree import ElementTree,Element
import xml.etree.ElementTree as ET

path=os.getcwd()
t = open(path+"/a000.txt")
def readXML():
    domTree = parse("/Users/zhaochen/Downloads/NLPP汉化/xml解析工具/a000.xml")
    rootNode = domTree.documentElement
    Dialog = rootNode.getElementsByTagName("Dialog")
    for Dia in range(len(Dialog)):
        Text = t.readline()
        Text = Text.replace("\n",'')
        rootNode.getElementsByTagName('Dialog')[Dia].childNodes[0].data=Text
    with open('a000.xml', 'w') as f:
        # 缩进 - 换行 - 编码
        domTree.writexml(f, addindent='  ', encoding='utf-8')
readXML()
t.close()
print('写入OK!')

