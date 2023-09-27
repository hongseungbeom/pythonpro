import random as rd
count = 1
herohp = rd.randrange(50,100)
mstrhp = rd.randrange(50,100)
print("hero HP :", herohp, ", monster HP : ", mstrhp)
  
while herohp > 0 and mstrhp > 0:
    herostr = rd.randrange(-10,20)
    mstrstr = rd.randrange(-10,20)
    herohp = herohp - mstrstr
    mstrhp = mstrhp - herostr
    print("hero(HP:", herohp, ", attack:", herostr,")", end=' ')
    if herostr > 0:
      print("success", end='')
    else:
      print("fail", end='')
    print("<-> monster(HP: ",mstrhp,", attack: ",mstrstr,")", end=' ')
    if mstrstr > 0:
      print("success")
    else:
      print("fail")
      
  
    count += 1
print("---------------------------------")
print("Total phase:",count,",")
if herohp > mstrhp:
    print("Hero Win!!!!")
else:
    print("Monster Win!!!!")
  
  
