import re

foo=open('sum.txt','r')
df=[]
while 1:
	linea=foo.readline()
	print(linea)
        if not linea: break
        f=re.split('\n',linea)
        print("f=",f)
        df.append(f[0])
foo.close()
print('df=',df)

sum=0
print(len(df))
for i in df:
  i=float(i)
  sum=sum+i

print("suma=",sum)
print("promedio=", sum/len(df))



