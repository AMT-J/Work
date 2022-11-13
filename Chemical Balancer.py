#coding=gbk
import easygui
N=100 #化学方程式长度
ma=[[0 for i in range(N)] for j in range(N)]#储存化成方程式出现的每个元素的个数
ma1=[[0 for i in range(N)] for j in range(N)]#增广矩阵
d1=[0 for i in range(N)] #储存矩阵的解
d2=[0 for i in range(N)] #记录原始化学方程式系数
elem={} #储存当前反应物(生成物)中每个元素的个数
s="" #储存化学方程式
s1=["" for i in range(N)] #储存化学方程式切片后的反应物和生成物(不含系数)
left_sum,right_sum=0,0 #分别储存反应物的个数、生成物的个数
iloc=0 #记录化学方程式等号的下标
Sum,D=0,0 #Sum=left_sum+right_sum,D为克莱姆法则中求解时的参数
flag=1 #判断是否有解，若有解则flag=1
CJ=""

def check(i):
    return 1 if i<left_sum else -1

def check1(k):
    return "" if k==1 else str(int(k))

def E_GetInt(temp,pos): #读取temp[pos]后的系数
    pos+=1;x=0
    if str.isdigit(temp[pos]):
        while(str.isdigit(temp[pos])):
            x=10*x+int(temp[pos])
            pos+=1
    else:
        x=1
    if temp[pos]=='+':
        return int(x)
    else :
        return int(-x)

def GetInt(temp,pos):
    pos+=1
    if str.islower(temp[pos]):
        pos+=1
    if not str.isdigit(temp[pos]):
        return 1
    else:
        x=0
        while str.isdigit(temp[pos]):
              x=10*x+int(temp[pos])
              pos+=1
        return int(x)


def gcd(a,b):#欧几里得求最大公约数
    return a if b==0 else gcd(b,a%b)

def determinant(n):#高斯消元法

    ans=1;v=1
    for i in range(n):
        for j in range(i+1,n):
            while ma1[i][i] :
                x=int(ma1[j][i]//ma1[i][i]) #辗转相除求整数解
                for k in range(i,n):
                    ma1[j][k]-=x*ma1[i][k]
                ma1[i],ma1[j]=ma1[j],ma1[i]
                v=-v 
            ma1[i],ma1[j]=ma1[j],ma1[i]
            v=-v
    for i in range(n):
        ans*=ma1[i][i]
    return int(ans*v)
def LegalCheck(s): #对读入的字符进行合法性判断
    if(40<=ord(s)<=41 or s=='+' or s=='-' or str.isalpha(s) 
    or str.isdigit(s) or 60<=ord(s)<=62 or s=='[' or s==']' ):
        return True
    return False

def Delspace(s):#删去字符串的多余的空格
    ans=""
    for i in range(len(s)):
        if LegalCheck(s[i]):
            ans+=s[i]
    return ans


def ToMatr():
    
    for i in range(Sum):#每次处理一个反应物(生成物)
        for j in elem:
            elem[j]=0
        temp=s1[i]
        k1=1;k2=1#k1记录()后的系数，k2记录[]后的系数
        for j in range(len(temp)):
            if temp[j]=='(':
                m=j+1
                while temp[m]!=')':
                    m+=1
                k1=GetInt(temp,m)
            if temp[j]==')':
                k1=1
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
                    elem[temp1]+=GetInt(temp,j)*k1*k2*check(i) #k1*k2可以解决括号嵌套
                else:
                    temp1=temp[j]
                    elem[temp1]+=GetInt(temp,j)*k1*k2*check(i)
            elif temp[j]=='<':
                elem["e"]=E_GetInt(temp,j)*check(i)
        x=0
        for cj in elem:
            ma[x][i]=elem[cj]
            x+=1

def solve():

    global flag
    flag=1
    ele=len(elem)
    for i in range(ele):
        ma[i][Sum-1]*=-1
    for i in range(Sum-1):#矩阵去重，将贡献为0的放到最后
        for j in range(i+1,ele):
            while ma[i][i]:
                x=int(ma[j][i]//ma[i][i])
                for k in range(i,Sum):
                    ma[j][k]-=x*ma[i][k]
                ma[i],ma[j]=ma[j],ma[i]
            ma[i],ma[j]=ma[j],ma[i]
    if Sum-ele>=2: #矩阵没有唯一整数解
        flag=0
        return 
    else:
        ele=min(ele,Sum-1)
        for i in range(ele):
            for j in range(ele):
                ma1[i][j]=ma[i][j]
        D=determinant(ele)#克莱姆法则
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
        for i in range(1,Sum):
            Gcd=gcd(Gcd,d1[i])
        if Gcd==0:
            flag=0
            return 
        for i in range(Sum):
            d1[i]/=Gcd
            if d1[i]<=0:
                flag=0
                return 

while True:
    #初始化
    s=""
    CJ="ERROR!"
    elem={}
    left_sum=right_sum=iloc=D=0
    for i in range(N):
        d1[i],d2[i]=0,1
        s1[i]=""
        for j in range(N):
            ma1[i][j],ma[i][j]=0,0

    s=easygui.enterbox("Please enter the chemical equation","Chemical Balancer",image="a.gif")
    
    if s=="":
        exit(0)
    s=Delspace(s)
    s+="%%%"#避免字符串下标溢出，方便处理
    for i in range(len(s)):#读取等号的下标，方便区分反应物和生成物以及后续矩阵归边的操作
            if s[i]=='=':
                iloc=i
                break

    if iloc!=0: 
        head=0 #当前反应物(生成物)的起始下标
        count=-1 #反应物(生成物)存放在s1中的下标
        for i in range(len(s)):
            if s[i]=='+' and s[i+1]!='>':
                if i <iloc:
                    left_sum+=1
                else:
                    right_sum+=1
                count+=1
                s1[count]=s[head:i]+"%%%"
                head=i+1
            if i ==iloc:
                count+=1
                s1[count]=s[head:i]+"%%%"
                head=i+1
            if i ==len(s)-1:
                count+=1
                s1[count]=s[head:]
        left_sum+=1;right_sum+=1
        Sum=left_sum+right_sum #反应物+生成物的总数量

        for  i in range(Sum):
            if  not str.isdigit(s1[i][0]):
                d2[i]=1 #记录原始化学方程式系数
            else:
                x,pos=0,0
                while str.isdigit(s1[i][pos]): #读取化学方程式的系数
                      x=10*x+int(s1[i][pos])
                      pos+=1
                d2[i]=x 
                m=len(str(x))
                s1[i]=s1[i][m:] #去除系数
        left_elem={};right_elem={}
        for i in range(len(s)):#记录化学方程式所有的元素(包括离子)
            temp=""
            if i <iloc:
                if str.isupper(s[i]):
                    if str.islower(s[i+1]):
                        temp=s[i]+s[i+1]
                        left_elem[temp]=0
                    else:
                        temp=s[i]
                    elem[temp]=0
                    left_elem[temp]=0
                elif s[i]=='<':
                    elem["e"]=0
                    left_elem["e"]=0
            else:
                if str.isupper(s[i]):
                    if str.islower(s[i+1]):
                        temp=s[i]+s[i+1]
                    else:
                        temp=s[i]
                    right_elem[temp]=0
                elif s[i]=='<':
                    right_elem["e"]=0
    
        ToMatr()
        solve()
        if not(right_elem and left_elem and right_elem==left_elem): flag=0
        if flag:
            cnt=0 
            while cnt < Sum:
                if d1[cnt]!=d2[cnt]:
                    break
                cnt+=1
            if cnt<Sum:
                CJ=""
                for i in range(Sum):
                    if i==left_sum-1:
                        CJ+=check1(d1[i])+s1[i][:-3]+" = "
                    elif i==Sum-1:
                        CJ+=check1(d1[i])+s1[i][:-3]
                    else:
                        CJ+=check1(d1[i])+s1[i][:-3]+" + "
            else:
                CJ="Has been balanced!"
    
    easygui.msgbox(msg=("The result are presented below:\n\n %s")%CJ)
