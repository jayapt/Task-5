
s= input( "Enter string:" )

dic={}

for c in s:
    dic[c]= dic.get ( c,0 ) + 1
    
print(dic)





