
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import random
import sys
a=10
b=10
l=25
alist = []
aa = 0
need = []
for j in range(2*a+1):
    if aa==0:
        aa = 1
        alistone = []
        for i in range(2*b+1):
            alistone.append(1)
        alist.append(alistone)
    else:
        aa=0
        alistone = []
        bb=0
        for i in range(2*b+1):
            if bb==0:
                bb=1
                alistone.append(1)
            else:
                bb = 0
                need.append((j,i))
                alistone.append(0)
        alist.append(alistone)
print(alist)
alist[0][1]=0
alist[-1][-2]=0
x=1
y=1
need.remove((1, 1))
listing=[]
while len(need)>0:
    aroundit=[]
    try:
        if x-2<0:
            print(1+"1")
        alist[x-2][y]=0
        if (x-2,y) in need:
            aroundit.append("alist[x-1][y],x=(0,x-2)")
    except:
        while False:
            print()
    try:
        alist[x+2][y]=0
        if (x+2,y) in need:
            aroundit.append("alist[x+1][y],x=(0,x+2)")
    except:
        while False:
            print()
    try:
        alist[x][y+2]=0
        if (x,y+2) in need:
            aroundit.append("alist[x][y+1],y=(0,y+2)")
    except:
        while False:
            print()
    try:
        if y-2<0:
            print(1+"1")
        alist[x][y-2]=0
        if (x,y-2) in need:
            aroundit.append("alist[x][y-1],y=(0,y-2)")
    except:
        while False:
            print()
    if len(aroundit)>0:
        listing.append((x,y))
        exec(random.choice(aroundit))
        need.remove((x, y))
    else:
        x,y=listing[-1]
        listing.pop()
x2=0
y2=1
listing2=[]
while not(alist[-1][-2]==2):
    alist[x2][y2]=3
    around2=[]
    try:
        if x2-1<0:
            print(1+"1")

        if alist[x2-1][y2]==0:
            around2.append("x2=x2-1")
    except:
        while False:
            print()
    try:

        if alist[x2+1][y2]==0:
            around2.append("x2=x2+1")
    except:
        while False:
            print()
    try:

        if alist[x2][y2+1]==0:
            around2.append("y2=y2+1")
    except:
        while False:
            print()
    try:
        if y2-1<0:
            print(1+"1")
        if alist[x2][y2-1]==0:
            around2.append("y2=y2-1")
    except:
        while False:
            print()
    if len(around2)>0:
        listing2.append((x2,y2))
        exec(random.choice(around2))
    else:
        alist[x2][y2]=2
        x2,y2=listing2[-1]
        listing2.pop()
alist[-1][-2]=3
for i in range(len(alist)):
    for j in range(len(alist[0])):
        if alist[i][j]==2:
            alist[i][j]=0
x = 1
y = 1
print("完成！")
