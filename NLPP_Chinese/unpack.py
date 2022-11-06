import os

path=os.getcwd()+"/Text/CHN"
path2=path+"/part/"
for file in os.listdir(path2):
    if file.split(".")[-1]=="txt":
        print(file)
        f=open(path2+file,'r')
        line = f.readline()
        line=f.readline()
        name=line.replace('\n','')
        T=open(path+"/"+name+".txt",'a')
        line=f.readline()
        print(name)
        while line:
            if line==" \n":
                T.close()
                line=f.readline()
                name=line.replace('\n','')
                T=open(path+"/"+name+".txt",'a')
                print(name)
                line=f.readline()
            else:
                line=line.replace("▲月▲日▲▲时▲","▲月▲▲日▲の▲時刻▲").replace("▲时间▲","▲時刻▲")
                line=line.replace("▲姐崎＊▲","▲姉ヶ崎＊▲").replace("▲姊崎＊▲","▲姉ヶ崎＊▲").replace("▲姐姐崎＊▲","▲姉ヶ崎＊▲")
                line=line.replace("姐姐崎＊▲","▲姉ヶ崎＊▲").replace("姐崎＊▲","▲姉ヶ崎＊▲")
                line=line.replace("高岭小路","高岭").replace("▲嶺＊＊▲","▲高嶺＊＊▲").replace("▲嶺＊▲","▲高嶺＊＊▲").replace("▲嶺＊＊＊▲","▲高嶺＊＊▲")
                line=line.replace("▲约会地点▲","▲デート場所▲")
                #▲彼女＊＊▲
                line=line.replace("隐马尔可夫模型","嗯").replace("福福","呼呼").replace("茨克","啧啧")
                line=line.replace("▲介绍朋友名▲","▲紹介友達名▲")
                line=line.replace("▲生成选项1▲","▲生成選択肢１▲")
                line=line.replace("▲高岭＊＊＊▲","▲高嶺＊＊▲").replace("▲高岭＊＊＊＊","▲高嶺＊＊▲").replace("▲高岭＊＊＊","▲高嶺＊＊▲")
                line=line.replace("小早川＊▲","▲小早川＊▲").replace("林科","凛子").replace("仁科","凛子")
                T.write(line)
                line=f.readline() 
  
        f.close()
print("完成")

