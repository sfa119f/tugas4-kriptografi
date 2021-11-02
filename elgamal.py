from function import isPrime
from math import pow
import random

def makePublicKey(p,g,x):
    if(isPrime(p) and g<p and x>=1 and x<=p-2):
        y = g ** x % p
        return y,g,p

def makePrivateKey(x,p):
    if(isPrime(p) and x>=1 and x<=p-2):
        return x,p

def makePlain(plainText):
    p = []
    plainText = plainText.upper()
    plain = list(plainText) 
    for char in plain:
        if (char.isalpha()):
            p.append(char)
        newP = "".join(p) 
    return newP

def encrypt(plainText, y, g, p):
    blockMessage = []
    for i in range (len(plainText)):
        blockMessage.append(ord(plainText[i])+ord('A'))
    print(blockMessage)
    # k = random.randint(0,p-1)
    k = 1520
    cipherA = g ** k % p
    listB = []
    for i in range (len(blockMessage)):
        b = y ** k * blockMessage[i] % p
        listB.append(str(b))
        print(listB)
        cipherB = "".join(listB)
    return cipherA, int(cipherB)

def decrypt(cipherA, cipherB, x, p):
    invAX = cipherA ** (p-1-x) % p
    cipherB = str(cipherB)
    cipherB = list(cipherB)
    msg = []
    for i in range (len(cipherB)):
        w = int(cipherB[i]) * invAX % p % 26
        msg.append(chr(w))
        m = "".join(msg)
    return m

print(encrypt("encrypt",1185,2,2357))
# print(decrypt(1430,7116111257187623226513301976338611,1751,2357))
# print(makePlain("encryption"))