def isPrime(n):
# Mengetahui apakah n adalah bilangan prima
  if n == 2 or n == 3: return True
  else if n < 2 or n % 2 == 0: return False
  else if n < 9: return True
  else if n % 3 == 0: return False
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
  return x * y / gcd(x, y)
