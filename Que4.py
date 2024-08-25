#string to upper case and a lower case 
def casechange(str):
    if(str.isupper()):
        
        str=str.lower()
    else:
        
        str=str.upper()
    return str
str=input()
print(casechange(str))