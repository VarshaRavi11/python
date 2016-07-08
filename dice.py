import random
i=0
j=0
s=0

print (i,j)

while ((i<8) and (j<8)):
    print "The value is...."
    val = random.randint(1,6)
    print val
    s=s+val
    if(i%2 == 0):
        if((j+val)<8):
            j=j+val-1
        else:
            x=7-j
            j=j+x
            i=i+1
            y=val-x
            j=j-y+1
    elif(i==8):
        if(j-val>0):
            j=j-val
        elif(j==0):
            print (i,j)
            print("you won") 
            break
        
        else:
            x=j-1
            if((j-val)>x-1):
                continue
            else:
                j=j-x-1
                y=val-x-1
                j=j+y
    else:
        if((j-val)>0):
            j=j-val
        else:
            x=j
            j=j-x
            i=i+1
            y=val-x 
            j=j+y
                    
        
   
   
                    
    print (i,j) 
            
                
        
