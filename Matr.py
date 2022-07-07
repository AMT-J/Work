from Algorithm import determinant, gcd
from Check import check
from GetInt import E_GetInt, GetInt

def ToMatr():
    global Sum,elem,s1
    for i in range(Sum):
        for j in elem.keys:
            elem[j]=0
        temp=s1[i]
        k1=1;k2=1
        for j in range(len(temp)):
            if temp[j]=='(':
                m=j+1
                while temp[m]!=')':
                    m+=1
                k1=GetInt(temp,m)
            if temp[j]==')':
                k=1
            if temp[j]=='[':
                m=j+1
                while temp[m]!=']':
                    m+=1
                k2=GetInt(temp,m)
            if temp[j]==']':
                k2=1
            if str.isupper(temp[j]):
                if str.islower(temp[j+1]):
                    temp1=temp[j]+temp[j+1]
                    elem[temp1]+=GetInt(temp,j)*k1*k2*check(i)
                else:
                    temp1=temp[j]
                    elem[temp1]+=GetInt(temp,j)*k1*k2*check(i)
            elif temp[j]=='<':
                elem["e"]=E_GetInt(temp,j)*check(i)
        x=0
        for i in elem.keys:
            ma[x][i]=elem[i]
            x+=1

def solve():
    global flag,elem,Sum,ma,ma1,d1
    flag=1
    ele=len(elem)
    for i in range(ele):
        ma[i][Sum-1]*=-1
    for i in range(Sum):
        for j in range(i+1,ele):
            while ma[i][i]:
                x=ma[j][i]//ma[i][i]
                for k in range(i,Sum):
                    ma[j][k]-=x*ma[i][k]
                ma[i],ma[j]=ma[j],ma[i]
            ma[i],ma[j]=ma[j],ma[i]
    if Sum-ele>=2:
        flag=0
        return 
    else:
        ele=min(ele,Sum-1)
        for i in range(ele):
            for j in range(ele):
                ma1[i][j]=ma[i][j]
        D=determinant(ele)
        for i in range(ele):
            for j in range(ele):
                for k in range(ele):
                    if k==i:
                        ma1[j][k]=ma[j][ele]
                    else:
                        ma1[j][k]=ma[j][k]
            d1[i]=determinant(ele)

        d1[Sum-1]=D 
        Gcd=d1[0]
        for i in range(1,sum):
            Gcd=gcd(Gcd,d1[i])
        if Gcd==0:
            flag=0
            return 
        for i in range(Sum):
            d1[i]/=Gcd
            if d1[i]<=0:
                flag=0
                return 
