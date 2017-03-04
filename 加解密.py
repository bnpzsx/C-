def encry(text,n ):
    result=''
    # text=text+"#"
    for i in text:
        try:  
            result=result + chr(ord(i)^n)
        except:
            result=result + chr(i^n)
        else:
            pass;
    return result

def decry(text,n):
    # text=text[0:-1]
    return encry(text,n)

def cchr(text,fgf):
    result=""
    asc=0
    for i in text:
        if i!=fgf :
            asc=asc*10+ord(i)-48
        else:
            # print(asc)
            result=result+chr(asc)
            asc=0
    return result

def  aasc(text,fgf):
    result=""
    for i in text:
        result=result+str(ord(i))+fgf
    return result
