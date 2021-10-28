def isPrime(n):
# Mengetahui apakah n adalah bilangan prima
  if n == 2 or n == 3: return True
  elif n < 2 or n % 2 == 0: return False
  elif n < 9: return True
  elif n % 3 == 0: return False
  else:
    maxVal = int(n**0.5)
    temp = 5
    while f <= maxVal:
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
