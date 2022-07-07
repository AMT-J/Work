
def E_GetInt(temp,pos):
    pos+=1;x=0
    if str.isdigit(temp[pos]):
        while(str.isdigit(temp[pos])):
            x=(x<<1)+(x<<3)+int(temp[pos])
            pos+=1
    else:
        x=1
    if temp[pos]=='+':
        return x
    else :
        return ~(x-1)

def GetInt(temp,pos):
    pos+=1
    if str.islower(temp[pos]):
        pos+=1
    if not str.isdigit(temp[pos]):
        return 1
    else:
        x=0
        while str.isdigit(temp[pos]):
              x=(x<<1)+(x<<3)+int(temp[pos])
              pos+=1
        return x


