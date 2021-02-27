carryLine = [False,False,False,False,False,False,False,False,False]
carryBit = [False,False,False,False,False,False,False,False]
input1 = [False,False,False,False,False,False,False,False]
input2 = [False,False,False,False,False,False,False,False]


#XOR Logic

def xor(i1,i2):
  if i1 == True or i2 == True:
    if not(i1 == True and i2 == True):
      return True
    else:
      return False
  else:
    return False


#Testing XOR
'''
print(str(xor(False,False)))
print(str(xor(True,False)))
print(str(xor(False,True)))
print(str(xor(True,True)))
'''
