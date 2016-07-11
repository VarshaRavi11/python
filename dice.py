import random
i=1
j=1
sr=0
sc=0
f=[[1 for x in range(9)] for y in range(9)]
print(i,j)

while ((i<=8) and (j<=8)):
     print "The value is...."  
     val = random.randint(1,6)
     print val
     if(i%2 != 0):
        if((j+val)<8):
            j=j+val
        else:
            x=8-j
            j=j+x
            i=i+1
            y=val-x-1
            j=j-y
     elif(i==8):
        if(j-val>0):
            j=j-val
       
        else:
            x=j-1
            j=j-x
            i=1
            y=val-x-1
            j=j+y
     else:
        if((j-val)>0):
            j=j-val
        else:        
            x=j-1
            j=j-x
            i=i+1
            y=val-x-1 
            j=j+y
                    
        
   
   
                    
     print (i,j) 
     f[i][j]=0
        
     for i in range(1, 8):
        for j in range(1, 8):
             if(f[i][j]==0):
                  sr+=1
             elif(f[j][i]==0):
                  sc+=1
        else:
            sc=0
            sr=0
    
             
     if(sr==8 or sc==8):
         
         print"BINGO"
         break
print f
     
              
    