
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

def determinant(n):
    global ma1,ma
    ans=1;v=1
    for i in range(n):
        for j in range(i+1,n):
            while ma1[i][i]!=0 :
                x=ma1[j][i]//ma1[i][i]
                for k in range(i,n):
                    ma1[j][k]-=x*ma1[i][k]
                ma1[i],ma1[j]=ma1[j],ma1[i]
                v=-v 
            ma1[i],ma1[j]=ma1[j],ma1[i]
    for i in range(n):
        ans*=ma1[i][i]
    ans*=v
    return ans

def Delspace(s):
    ans=""
    for i in range(len(s)):
        if s[i]!=' ':
            ans+=s[i]
    return ans
