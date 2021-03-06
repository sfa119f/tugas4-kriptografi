from function import *

def isRsaValidatePQ(pValue, qValue):
# Mengvalidasi nilai P dan Q RSA
  if isPrime(pValue) and isPrime(qValue):
    return True
  return False

def isRsaValidateEkey(eKey, pValue, qValue):
# Mengvalidasi nilai key E RSA
  phi = (pValue - 1) * (qValue - 1)
  if gcd(eKey, phi) == 1:
    return True
  return False

def makePbKeyRsa(pValue, qValue, eKey):
# Menghitung public key algoritma RSA
  return eKey, (pValue * qValue)

def makePvKeyRsa(pValue, qValue, eKey):
# Menghitung private key algoritma RSA
  phi = (pValue - 1) * (qValue - 1)
  cek = True
  k = 1
  while cek:
    if (1 + (k * phi)) / eKey == (1 + (k * phi)) // eKey: cek = False
    else: k += 1
  return (1 + (k * phi)) // eKey, (pValue * qValue)

def methodRsa(nValue, key, text, isEncrypt):
# Mengenkripsi atau mendeskripsi text menggunakan algoritma RSA
  lenVal = lenValCipher(nValue)
  if isEncrypt: valArray = makeBlockMessage(lenVal, text)
  else: valArray = strToBlockCipher(lenVal, text)
  res = []
  for i in range(len(valArray)):
    res.append(valArray[i] ** key % nValue)
  if isEncrypt: return blockCipherToStr(lenVal, res)
  else: return blockMessageToText(lenVal, res)
