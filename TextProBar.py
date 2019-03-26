#TextProBar.py 文本进度条
#刷新的本质：用后打印的信息覆盖之前的
# \r 输出前光标退回行首
import time
scale = 50
print("执行开始".center(scale//2,"-"))   #使用.center()填充在“执行开始”两边
start = time.perf_counter()   #计时
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)

print("\n"+"执行结束".center(scale//2),"-")
