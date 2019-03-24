#AutoTraceDraw.py

import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

#数据读取,解析数据并存入列表
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))  #map函数--将第一个参数的功能作用于第二个参数的每一个元素
f.close()

#自动绘制
for i in range((len(datals))):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

t.done()

'''  #data.txt
300,0,144,1,0,0
300,0,144,0,1,0
300,0,144,0,0,1
300,0,144,1,1,0
300,0,108,0,1,1
184,0,72,1,0,1
184,0,72,0,0,0
184,0,72,0,0,0
184,0,72,0,0,0
184,1,72,1,0,1
184,1,72,0,0,0
184,1,72,0,0,0
184,1,72,0,0,0
184,1,72,0,0,0
184,1,720,0,0,0
'''
