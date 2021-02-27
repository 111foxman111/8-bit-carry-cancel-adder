#XOR Logic

def xor(i1,i2):
  if i1 == True or i2 == True:
    if not(i1 == True and i2 == True):
      return True
    else:
      return False
  else:
    return False

#AND Logic

def a(i1,i2):
  if i1 == True and i2 == True:
    return True
  else:
    return False

#OR Logic

def o(i1,i2):
  if i1 == True or i2 == True:
    return True
  else:
    return False

#Testing XOR
'''
print(str(xor(False,False)))
print(str(xor(True,False)))
print(str(xor(False,True)))
print(str(xor(True,True)))
'''

#Single Adder Logic

def fullAdder(i1,i2,c):
  r = xor(xor(i1,i2),c)
  co = o(a(i1,i2),a(c,xor(i1,i2)))
  return r,co;

#Tests

'''
print('Result: ' + str(int(fullAdder(1,1,0)[0])) + ' Carry: ' + str(int(fullAdder(1,1,0)[1])))
'''

result = [False,False,False,False,False,False,False,False]
carry = [False,False,False,False,False,False,False,False]

def fourBitAdder(l1,l2,carryIn):
  result[0] = fullAdder(l1[0],l2[0],carryIn)[0]
  carry[0] = fullAdder(l1[0],l2[0],carryIn)[1]
  result[1] = fullAdder(l1[1],l2[1],carry[0])[0]
  carry[1] = fullAdder(l1[1],l2[1],carry[0])[1]
  result[2] = fullAdder(l1[2],l2[2],carry[1])[0]
  carry[2] = fullAdder(l1[2],l2[2],carry[1])[1]
  result[3] = fullAdder(l1[3],l2[3],carry[2])[0]
  print(str(int(result[3]))+str(int(result[2]))+str(int(result[1]))+str(int(result[0])))

input1 = [True,True,True,False,True,True,False,True]
input2 = [False,True,True,False,False,False,False,False]

#fourBitAdder(input1,input2,False)

def eightBitAdder(l1,l2,carryIn,shiftDown,shiftUp,sub):
  result[0] = fullAdder(l1[0],l2[0],carryIn)[0]
  carry[0] = fullAdder(l1[0],l2[0],carryIn)[1]
  result[1] = fullAdder(l1[1],l2[1],carry[0])[0]
  carry[1] = fullAdder(l1[1],l2[1],carry[0])[1]
  result[2] = fullAdder(l1[2],l2[2],carry[1])[0]
  carry[2] = fullAdder(l1[2],l2[2],carry[1])[1]
  result[3] = fullAdder(l1[3],l2[3],carry[2])[0]
  carry[3] = fullAdder(l1[3],l2[3],carry[2])[1]
  result[4] = fullAdder(l1[4],l2[4],carry[3])[0]
  carry[4] = fullAdder(l1[4],l2[4],carry[3])[1]
  result[5] = fullAdder(l1[5],l2[5],carry[4])[0]
  carry[5] = fullAdder(l1[5],l2[5],carry[4])[1]
  result[6] = fullAdder(l1[6],l2[6],carry[5])[0]
  carry[6] = fullAdder(l1[6],l2[6],carry[5])[1]
  result[7] = fullAdder(l1[7],l2[7],carry[6])[0]
  carry[7] = fullAdder(l1[7],l2[7],carry[6])[1]
  
  if shiftDown and shiftUp:
    result[0] = result[0]

  elif shiftDown:
    result[0] = result[1]
    result[1] = result[2]
    result[2] = result[3]
    result[3] = result[4]
    result[4] = result[5]
    result[5] = result[6]
    result[6] = result[7]
    result[7] = False

  elif shiftUp:
    result[7] = result[6]
    result[6] = result[5]
    result[5] = result[4]
    result[4] = result[3]
    result[3] = result[2]
    result[2] = result[1]
    result[1] = result[0]
    result[0] = carryIn

  print(str(int(result[7]))+str(int(result[6]))+str(int(result[5]))+str(int(result[4]))+str(int(result[3]))+str(int(result[2]))+str(int(result[1]))+str(int(result[0])))

'''
eightBitAdder(input1,input2,False,False,False)
eightBitAdder(input1,input2,False,True,True)
eightBitAdder(input1,input2,False,False,True)
eightBitAdder(input1,input2,False,True,False)
'''

def twoCompliment(inp1):
  print([not elem for elem in inp1])
  return [not elem for elem in inp1]

def subtract(i1,i2): #DOES NOT WORK NEEDS TO BE FIXED
  eightBitAdder(twoCompliment(i1),i2,True,False,False,True)

def add(i1,i2):
  eightBitAdder(i1,i2,False,False,False,False)

add([True,False,True,False,False,True,False,False],[True,False,True,False,False,True,False,False])

subtract([True,False,True,False,False,True,False,False],[False,False,False,False,False,False,False,True])
