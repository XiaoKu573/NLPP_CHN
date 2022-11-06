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
    
path=os.getcwd()+"/Text/ENG"
q=0
n=0
for file in os.listdir(path):
    f=open(path+"/part/packENG_Part"+str(q)+".txt",'a')
    if file.split(".")[-1]=="txt":
        path2=path+"/"+file
        optxt()
        n=n+1
        if n==34:
            q=q+1
            n=0
f.close()
print("完成")
