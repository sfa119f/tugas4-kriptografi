def makePbKeyRsa(pValue, qValue, eKey):
# Menghitung public key algoritma RSA
  return eKey, (pValue * qValue)

def makePvKeyRsa(pValue, qValue, eKey):
# Menghitung private key algoritma RSA
  phi = (pValue - 1) * (qValue - 1)
  cek = True
  k = 1
  while cek:
    print((1 + (k * phi)) / eKey)
    if (1 + (k * phi)) / eKey == (1 + (k * phi)) // eKey: cek = False
    else: k += 1
  return (1 + (k * phi)) // eKey, (pValue * qValue)

def blockMessage(n):
  if n == 0: return 0
  if n == 1: return 10
  else: return blockMessage(n - 2) * 100 + 25

def methodRsa(nValue, key, text):
# Mengenkripsi atau mendeskripsi text menggunakan algoritma RSA
  if nValue < 25:
    lenVal = 1
  else:
    lenVal = 2
    while blockMessage(lenVal + 2) < nValue:
      lenVal += 2
  
  if len(text) % (lenVal // 2) != 0:
    text += 'X' * ((lenVal // 2) - (len(text) % (lenVal // 2)))

  res = ''
  for i in range(0, len(text), (lenVal // 2)):
    if lenVal == 1:
      res += chr(((((ord(text[i]) - ord('A')) // 10) ** key) % nValue + ord('A')) * 10 + ((((ord(text[i]) - ord('A')) % 10) ** key) % nValue + ord('A')))
    else:
      blockDigit = 0
      for j in range(i, i + (lenVal // 2)):
        blockDigit = blockDigit * 100 + (ord(text[j]) - ord('A'))
      resDigit = blockDigit ** key % nValue
      tres = ''
      if resDigit // (10 ** (lenVal - 2)) == 0:
        tres = 'A'
      while resDigit != 0:
        tres = chr(resDigit % 100 + ord('A')) + tres
        resDigit //= 100
      res += tres
  return res
