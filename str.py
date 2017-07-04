#!coding=utf-8
str='hello word ,aa bb cc aa bb cc aa bb cc cd cc aa aa cc cc cc aa aa'
mylist=str.split(' ')
num=[]
for key in mylist:
    num.append(str.count(key))
    #print num
    if max(num)==str.count(key):
        maxnum=max(num)
        maxkey=key
print 'the words maxnum is %s ,number :%d'%(maxkey,maxnum)
