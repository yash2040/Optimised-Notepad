def encoder(s):
    dict = {}
    for i in range(0, 256):
        dict[chr(i)] = i
    p = ""
    c = ""
    p += s[0]
    code = 256
    output_code = []
    for i in range(0, len(s)):
        if i != len(s) - 1:
            c += s[i + 1]
        if (p + c) in dict:
            p = p + c
        else:
            output_code.append(dict[p])
            dict[p + c] = code
            code = code + 1
            p = c
        c = ""
    output_code.append(dict[p])
    ans=""
    for i in range(0,len(output_code)):
        if i==len(output_code)-1:
            ans=ans+str(output_code[i])
        else:
            ans=ans+str(output_code[i])+' '
    return ans

def decoder(output_code):
    ans=""
    dict={}
    for i in range(0,256):
        dict[i]=chr(i)
    old=output_code[0]
    s=dict[old]
    c=""
    c=c+s[0]
    ans=ans+s
    count=256
    for i in range(0,len(output_code)-1):
        n=output_code[i+1]
        if n in dict:
            s=dict[n]
        else:
            s=dict[old]
            s=s+c
        ans=ans+s
        c=""
        c=c+s[0]
        dict[count]=dict[old]+c
        count=count+1
        old=n
    print("decoded")
    return ans