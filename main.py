#coding=gbk
N=100
ma=[[0 for i in range(N)] for j in range(N)]
ma1=[[0 for i in range(N)] for j in range(N)]
d1=[0 for i in range(N)]
d2=[0 for i in range(N)]
elem={}
s=""
s1=["" for i in range(N)]
left_sum,right_sum=0,0
iloc=0
Sum,D=0,0
flag=1

from GetInt import *
from Check import *
from Algorithm import *
from Matr import *
while True:
    s=""
    elem={}
    left_sum=right_sum=iloc=D=0
    for i in range(N):
        d1[i],d2[i]=0,1
        s1[i]=""
        for j in range(N):
            ma1[i][j],ma[i][j]=0,0

    s=input("Enter Here:")
    s=Delspace(s)
    for i in range(len(s)):
            if s[i]=='=':
                iloc=i
                break

    head=0
    count=-1
    for i in range(len(s)):
        if s[i]=='+' and s[i+1]!='>':
            if i <iloc:
                left_sum+=1
            else:
                right_sum+=1
            count+=1
            s1[count]=s[head:i]
            head=i+1
        if i ==iloc:
            count+=1
            s1[count]=s[head:i]
            head=i+1
        if i ==len(s)-1:
            count+=1
            s1[count]=s[head:]
    left_sum+=1;right_sum+=1
    Sum=left_sum+right_sum 

    for  i in range(Sum):
        if str.isdigit(s1[i][0]):
            d2[i]=1
        else:
            x,pos=0,0
            while str.isdigit(s1[i][pos]):
                  x=(x<<1)+(x<<3)+int(s1[i][pos])
                  pos+=1
            d2[i]=x 
            m=str(x)
            s1[i]=s1[i][len(m):]

    for i in range(iloc):
        temp=""
        if str.isupper(s[i]):
            if str.islower(s[i+1]):
                temp=s[i]+s[i+1]
            else:
                temp=s[i]
        elif s[i]=='<':
                elem["e"]=0
    
    ToMatr()
    solve()
    if flag:
        cnt=0 
        for cnt in range(Sum):
            if d1[cnt]!=d2[cnt]:
                break
        if cnt<Sum:
            print("Result:",end="")
            for i in range(Sum):
                if i==left_sum-1:
                    print(check1(d1[i]),end="")
                    print(s1[i],end="=")
                elif i==Sum-1:
                    print(check1(d1[i]),end="")
                    print(s1[i])
                else:
                    print(check1(d1[i]),end="")
                    print(s1[i],end="+")
        else:
            print("Have been balanced")
    else:
        print("ERROR")
