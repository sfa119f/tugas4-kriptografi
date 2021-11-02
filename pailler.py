from function import gcd, lcm, invMod

def isPaillerValidatePQ(pValue, qValue):
  if gcd((pValue * qValue), ((pValue - 1) * (qValue - 1))) == 1 && pValue * qValue >= 256:
    return True
  return False

def isPaillerValidateG(gValue, nValue):
  if gValue < (nValue ** 2):
    return True
  return False

def isPaillerValidateR(rValue):
  if gcd(rValue, nValue) == 1 && rValue >= 0 && rValue < nValue:
    return True
  return False

def functionL(x, nValue):
  return (x - 1) // nValue

def makePbKeyPailler(pValue, qValue, gValue):
# Menghitung public key algoritma Pailler
  return gValue, (pValue * qValue)

def makePvKeyPailler(pValue, qValue, gValue):
# Menghitung private key algoritma Pailler
  nValue = pValue * qValue
  lamda = lcm(pValue - 1, qValue - 1)
  mu = invMod(functionL((gValue ** lamda) % (nValue ** 2), nValue), nValue)
  return lamda, mu

def methodPailler(keyA, keyB, text, encrypt, rValue = None, nValue = None):
  res = ''
  if encrypt:
    for i in range(len(text)):
      temp = ord(text[i])
      print(((keyA ** temp) * (rValue ** keyB)) % (keyB ** 2))
      res += chr(((keyA ** temp) * (rValue ** keyB)) % (keyB ** 2))
  else:
    for i in range(len(text)):
      temp = ord(text[i])
      res += chr((functionL((temp ** keyA) % (nValue ** 2), nValue) * keyB) % nValue)
      print((functionL((temp ** keyA) % (nValue ** 2), nValue) * keyB) % nValue)
  return res

g, n = makePbKeyPailler(17, 23, 5652)
lamda, mu = makePvKeyPailler(17, 23, 5652)
print('g', g, 'n', n)
print('lamda', lamda, 'mu', mu)
en = methodPailler(g, n, 'INDOMIE', True, rValue=37)
print(en)
de = methodPailler(lamda, mu, en, False, nValue=n)
print(en, de)