target=int(input('请输入一个目标值'))

a=[8,4,0,2,9,5,3,9,6]

b=len(a)
#print(b)
for i in range(0,b-1):

    for j in range(i+1,b):

        sum=a[i]+a[j]
        # print('和为',sum)

        if  sum== target:
            print('对应的下标分别为',i,j) 