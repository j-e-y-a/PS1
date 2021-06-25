#Qs 3c 

import numpy as np
#initial internal node temperatures
T_11 = 0
T_12 = 0
T_13 = 0
T_14 = 0

T_21 = 0
T_22 = 0
T_23 = 0
T_24 = 0

T_31 = 0
T_32 = 0
T_33 = 0
T_34 = 0

#initial error
Ea = 100

#iteration
i = 0

print ('Ea')
print ('')

while Ea > 1:
    Ea = 0
    T_11new=(75+50+T_21+T_12)/4
    Ea_new=((T_11new-T_11)/T_11new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_11=T_11new
        
    T_12new=(75+T_11+T_22+T_13)/4
    Ea_new=((T_12new-T_12)/T_12new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_12=T_12new
    
    T_13new=(75+T_12+T_23+T_14)/4
    Ea_new=((T_13new-T_13)/T_13new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_13=T_13new
    
    T_14new=(75+T_13+T_24+100)/4
    Ea_new=((T_14new-T_14)/T_14new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_14=T_14new
    
    T_21new=(50+T_11+T_22+T_31)/4
    Ea_new=((T_21new-T_21)/T_21new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_21=T_21new
    
    T_22new=(T_21+T_12+T_23+T_32)/4
    Ea_new=((T_22new-T_22)/T_22new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_22=T_22new
    
    T_23new=(T_22+T_13+T_24+T_33)/4
    Ea_new=((T_23new-T_23)/T_23new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_23=T_23new
    
    T_24new=(T_23+T_14+100+T_34)/4
    Ea_new=((T_24new-T_24)/T_24new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_24=T_24new
    
    T_31new=(50+T_21+T_32+100)/4
    Ea_new=((T_31new-T_31)/T_31new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_31=T_31new
    
    T_32new=(T_31+T_22+T_33+100)/4
    Ea_new=((T_32new-T_32)/T_32new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_32=T_32new
    
    T_33new=(T_32+T_23+T_34+100)/4
    Ea_new=((T_33new-T_33)/T_33new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_33=T_33new
    
    T_34new=(T_33+T_24+100+100)/4
    Ea_new=((T_34new-T_34)/T_34new)*100
    if Ea_new>Ea:
        Ea=Ea_new
    else:
        Ea=Ea
    T_34=T_34new
    
    i=i+1
    
    print (Ea)

print ('')
print ('T (1,1):',T_11)
print ('T (1,2):',T_12)
print ('T (1,3):',T_13)
print ('T (1,4):',T_14)
print ('T (2,1):',T_21)
print ('T (2,2):',T_22)
print ('T (2,3):',T_23)
print ('T (2,4):',T_24)
print ('T (3,1):',T_31)
print ('T (3,2):',T_32)
print ('T (3,3):',T_33)
print ('T (3,4):',T_34)
print('')
print (i,'iterations take to get all of the temperatures values within 1% error')