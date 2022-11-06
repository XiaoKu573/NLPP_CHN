from xml.dom.minidom import parse
import os, xml.dom.minidom
from xml.etree.ElementTree import ElementTree,Element
import xml.etree.ElementTree as ET

def readXML():
    domTree = parse(pathxml+"/"+file)
    rootNode = domTree.documentElement
    Dialog = rootNode.getElementsByTagName("Dialog")
    for Dia in range(len(Dialog)):
        Text = t.readline()
        Text = Text.replace("\n",'')
        rootNode.getElementsByTagName('Dialog')[Dia].childNodes[0].data=Text
    with open(pathout+file, 'w') as f:
        # 缩进 - 换行 - 编码
        domTree.writexml(f, addindent='  ', encoding='utf-8')

path=os.getcwd()+"/Text/CHN/"
pathxml=os.getcwd()+"/xml/ENG"
pathout=os.getcwd()+"/xml/CHN/"
for file in os.listdir(pathxml):
    if file.split(".")[-1]=="xml":
        t = open(path+file.replace("xml","txt"))
        readXML()
        t.close()
print('写入OK!')

