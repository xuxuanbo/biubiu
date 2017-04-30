#-*-coding:utf-8
import jieba
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs
g=[]

def a(path,str,list):
 with codecs.open(path,'r','utf-8')as a:
    for line in a.readlines():
        line=line.strip('\n')
        list.append((line,str))

a('/home/xuxuanbo/桌面/week2/homework/词典/制作/编剧.txt','编剧',g)
b=codecs.open('/home/xuxuanbo/桌面/cesh.txt','a','utf-8')
e=dict(g)
l=''
with codecs.open(('/home/xuxuanbo/桌面/太空旅客.txt'), 'r', 'utf-8')as c:
    for line in c.readlines():
        line=line.strip('\n')
        l=l+line
h={'编剧':0}
d=jieba.cut(l)
for i in d:
    if i in e.keys():
        h['编剧']+=1

print h['编剧']
#接下来只要依次输入每个文件的名字，并依次调用函数a，就可以计算出每一个文件中评论的涉及数，对这些数字进行比对，就可以粗略地看出评论的关注点。


