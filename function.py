def isPrime(n):
# Mengetahui apakah n adalah bilangan prima
  if n == 2 or n == 3: return True
  elif n < 2 or n % 2 == 0: return False
  elif n < 9: return True
  elif n % 3 == 0: return False
  else:
    maxVal = int(n**0.5)
    temp = 5
    while temp <= maxVal:
      if n % temp == 0: return False
      if n % (temp + 2) == 0: return False
      temp += 6
    return True

def gcd(x, y):
# Menghitung fpb dari x dan y
  if(y == 0):
    return x
  else:
    return gcd(y, x % y)

def lcm(x, y):
# Menghitung kpk dari x dan y
  return x * y // gcd(x, y)

def invMod(val1, val2):
# Menghitung invers modulo
  a, b, x, y, u, v =  val1, val2, 0, 1, 1, 0
  while a != 0:
    q = b // a
    r = b % a
    m = x - u * q
    n = y - v * q
    b, a, x, y, u, v = a, r, u, v, m, n
  if b != 1:
    return None
  return x % val2

def blockMessage(n):
# Value block message dengan panjang n
  if n == 0: return 0
  if n == 1: return 10
  else: return blockMessage(n - 2) * 100 + 25

def lenValCipher(n):
# Menghitung panjang hasil dari cipher text
  if n < 25:
    lenVal = 1
  else:
    lenVal = 2
    while blockMessage(lenVal + 2) < n:
      lenVal += 2
  return lenVal

def makeBlockMessage(lenVal, text):
# Membuat block message dari text dengan panjang lenVal
  if len(text) % (lenVal // 2) != 0:
    text += 'X' * ((lenVal // 2) - (len(text) % (lenVal // 2)))

  res = []
  for i in range(0, len(text), (lenVal // 2)):
    if lenVal == 1:
      res.append(ord(text[i]) - ord('A') // 10)
      res.append(ord(text[i]) - ord('A') % 10)
    else:
      blockDigit = 0
      for j in range(i, i + (lenVal // 2)):
        blockDigit = blockDigit * 100 + (ord(text[j]) - ord('A'))
      res.append(blockDigit)
  
  return res

def blockMessageToText(lenVal, mArray):
# Convert block message to text
  res = ''
  i = 0
  while i < len(mArray):
    if lenVal == 1:
      res += chr(mArray[i] * 10 + mArray[i+1])
      i += 2
    else:
      tres1 = ''
      if mArray[i] // (10 ** (lenVal - 2)) == 0:
        tres2 = 'A'
      else: tres2 = ''
      while mArray[i] != 0:
        tres1 = chr(mArray[i] % 100 + ord('A')) + tres1
        mArray[i] //= 100
      res += (tres2 + tres1)
      i += 1
  return res

def blockCipherToStr(lenVal, cArray):
# Membuat semua panjang dari blok cipher menjadi sama panjang
  res = ''
  for i in range(len(cArray)):
    temp = ''
    for j in range(lenVal - len(str(cArray[i]))):
      temp += '0'
    res += (temp + str(cArray[i]))
  return res

def strToBlockCipher(lenVal, strNum):
# Mengembalikan panjang dari masing-masing blok cipher ke semula
  temp = 10 ** lenVal
  res = []
  while len(strNum) != 0:
    val = int(strNum[:lenVal])
    strNum = strNum[lenVal:]
    res.append(val)
  return res

def makePlain(plainText):
# Membuat plainText sesuai dengan format yang diinginkan yakni
# menghilangkan angka dan symbol serta membuat huruf menjadi uppercase
    p = []
    plainText = plainText.upper()
    plain = list(plainText) 
    for char in plain:
        if (char.isalpha()):
            p.append(char)
        newP = "".join(p) 
    return newP