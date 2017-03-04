def encry(text,n ):
    result=""
    # text=text+"#"
    for i in text:
        result=result + chr(ord(i)^n)
    return result
def decry(text,n):
    # text=text[0:-1]
    return encry(text,n)
    
