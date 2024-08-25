#find the substring in the program
def substr(str,sustr):
    result=""
    for i in range(0,len(str)):
        if str[i]==sustr[0]:
            for j in range(0,len(sustr)):
                if(str[i]==sustr[j]):
                    i+=1
                    result=result+sustr[j]
    if(result==sustr):
        return "true"
    else:
        return result
print(substr("zeael","el") )             
                

