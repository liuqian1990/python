arr = [1,2,8,5,4,3]
for i in range(0,len(arr)/2):
      arr[i], arr[-i - 1] = arr[-i -1], arr[i] // a,b = b,a 交换 索引值相加等于-1就交换
print arr
