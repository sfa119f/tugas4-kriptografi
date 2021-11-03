from function import gcd, lcm, invMod, lenValCipher, makeBlockMessage, blockCipherToStr, strToBlockCipher, blockMessageToText

def isPaillerValidatePQ(pValue, qValue):
  if gcd((pValue * qValue), ((pValue - 1) * (qValue - 1))) == 1 and pValue * qValue >= 256:
    return True
  return False

def isPaillerValidateG(gValue, nValue):
  if gValue < (nValue ** 2):
    return True
  return False

def isPaillerValidateR(rValue):
  if gcd(rValue, nValue) == 1 and rValue >= 0 and rValue < nValue:
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
  res = []
  if encrypt:
    mArray = makeBlockMessage(lenValCipher(keyB), text)
    for i in range(len(mArray)):
      res.append((keyA ** mArray[i]) * (rValue ** keyB) % (keyB ** 2))
    return blockCipherToStr(lenValCipher(keyB ** 2 * 100), res)
  else:
    cArray = strToBlockCipher(lenValCipher(nValue ** 2 * 100), text)
    for i in range(len(cArray)):
      res.append((functionL((cArray[i] ** keyA) % (nValue ** 2), nValue) * keyB) % nValue)
    return blockMessageToText(lenValCipher(nValue), res)
