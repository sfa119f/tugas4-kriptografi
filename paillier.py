from function import gcd, lcm, invMod, lenValCipher, makeBlockMessage, blockCipherToStr, strToBlockCipher, blockMessageToText

def isPaillierValidatePQ(pValue, qValue):
# Mengvalidasi nilai P dan Q Paillier
  if gcd((pValue * qValue), ((pValue - 1) * (qValue - 1))) == 1 and pValue * qValue >= 256:
    return True
  return False

def isPaillierValidateG(gValue, nValue):
# Mengvalidasi nilai G Paillier
  if gValue < (nValue ** 2):
    return True
  return False

def isPaillierValidateR(rValue):
# Mengvalidasi nilai R Paillier
  if gcd(rValue, nValue) == 1 and rValue >= 0 and rValue < nValue:
    return True
  return False

def functionL(x, nValue):
# Menghitung fungsi L(x) Paillier
  return (x - 1) // nValue

def makePbKeyPaillier(pValue, qValue, gValue):
# Menghitung public key algoritma Paillier
  return gValue, (pValue * qValue)

def makePvKeyPaillier(pValue, qValue, gValue):
# Menghitung private key algoritma Paillier
  nValue = pValue * qValue
  lamda = lcm(pValue - 1, qValue - 1)
  mu = invMod(functionL((gValue ** lamda) % (nValue ** 2), nValue), nValue)
  return lamda, mu

def methodPaillier(keyA, keyB, text, encrypt, rValue = None, nValue = None):
# Mengenkripsi atau mendeskripsi text menggunakan algoritma Paillier
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
