def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n % 2 == 0: return False
  if n < 9: return True
  if n % 3 == 0: return False
  maxVal = int(n**0.5)
  temp = 5
  while f <= maxVal:
    if n % temp == 0: return False
    if n % (temp + 2) == 0: return False
    temp += 6
  return True
