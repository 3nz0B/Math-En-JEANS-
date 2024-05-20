powerNum = 3
loopNumber = 3
runs = 0
amtOfZeros = 12

while loopNumber != (amtOfZeros-1)*'0'+'1':
  runs+=1
  loopNumber = str(int(loopNumber) *3)[-amtOfZeros:]
for i in range(amtOfZeros+1) :
  powerNum=(3**(powerNum%(runs+1) ))%10**amtOfZeros
  print (powerNum)
