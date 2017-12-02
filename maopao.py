http://pythontutor.com/visualize.html#mode=edit
heigh = [9,8,7,6,5,4]

count = 0 //优化,计算循环次
for j in range(0,len(heigh)-1):
    for i in range(0,len(heigh)-1):
          if heigh[i] > heigh[i+1]:                       
                heigh[i],heigh[i+1] = heigh[i+1],heigh[i] // a,b = b,a 两位置交换
print heigh

heigh = [9,8,7,6,5,4]
heigh = [8,9,7,6,5,4]
heigh = [8,7,9,6,5,4]
heigh = [8,7,6,9,5,4]
heigh = [8,7,6,5,9,4]
heigh = [8,7,6,5,4,9]