import urllib.request
import datetime
import shutil
import os
dir='C:\\Users\\T180P\\Desktop\\Tong\\WixWeb\\Pictures\\chocalate\\'
shutil.rmtree(dir)
os.makedirs(dir)
with open('ImageUrls', 'r') as imgfile:
    ss=imgfile.readlines()
for i in ss:
    imgname='C'+str(datetime.datetime.today()).replace(':','_')+'.jpg'
    print(imgname,i)
    urllib.request.urlretrieve(i,dir+imgname)