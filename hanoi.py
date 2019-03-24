#hanoi
'''
A，B，C三个圆柱，分别为初始位，过渡位，目标位，设A柱为初始位，C位为最终目标位
（1）将最上面的n-1个圆盘从初始位移动到过渡位
（2）将初始位的最底下的一个圆盘移动到目标位
（3）将过渡位的n-1个圆盘移动到目标位
对于递归算法中的嵌套函数f（n-1）来说，其初始位，过渡位，目标位发生了变化
'''
count = 0

def hanoi(n,src,dst,mid):   #n为圆盘数，src代表初始位圆柱，dst代表过渡位圆柱，mid代表目标位圆柱
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))  #把1号圆盘从 src 搬到 dst
        count += 1
    else:
        hanoi(n-1,src,mid,dst)  #将初始位的n-1个圆盘移动到过渡位，此时初始位为src，上一级函数的过渡位dst即为本级的目标位，上级的目标位mid为本级的过渡位
        print("{}:{}->{}".format(n,src,dst))  #把n号圆盘从 src 搬到 dst
        count +=1
        hanoi(n-1,mid,dst,src) #将过渡位的n-1个圆盘移动到目标位，此时初始位为dst，上一级函数的目标位mid即为本级的目标位，上级的初始位src为本级的过渡位

hanoi(3,"A","C","B")
print(count)
