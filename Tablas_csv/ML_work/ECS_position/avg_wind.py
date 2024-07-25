
wd=[2,0,0,4,0,0,0,6,0,0,0,8]

#wd=['3','7']

wdp=[]
j=0
wind=[]
for i in range(len(wd)):
    #print("posicion de i=",i)  
    if wd[i]==0:
        print("posicion de i=",i)
        print("average= ",prom)
        wind.append(prom)
    if wd[i] > 0:
        wind.append(wd[i])
        print("wd[i]: ",wd[i])
        V1=wd[i]
        if wd.index(wd[-1])== j:
            break
        j=j+1
        #print("j1=",j)
        while wd[j]==0:
            j=j+1
            #print("j2=",j)
        if wd[j] >0:
            V2=wd[j]
        print("V1,V2: ", V1,V2)
        prom=(V1+V2)/2
        #print("promedio=",prom)
        
        
print("wind= ",wind)
    
