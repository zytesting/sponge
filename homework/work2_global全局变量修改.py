#coding:utf-8

#2、如何在一个函数内部修改全局变量，利用global 修改全局变量


age = 10

print('方法外没使用global，age的值',age)


def testModify():

    global age

    print('未赋值前age为',age)

    age=30

    print('方法内赋值后age值为',age)

testModify()

print('方法外用了global后age的值',age)



