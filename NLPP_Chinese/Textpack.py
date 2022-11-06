import os

def optxt():
    T=open(path2)
    num=file.split(".")[0]
    f.write('\n'+num+'\n')
    Text = T.readline()
    while Text:
        f.write(Text)
        Text = T.readline()
    T.close()
    
path=os.getcwd()+"/Text/JPN"
for file in os.listdir(path):
    if file.split(".")[-1]=="txt":
        print(file)
        path2=path+"/"+file
        f=open(path+"/packJPN.txt",'a')
        optxt()
        
f.close()
print("完成")
