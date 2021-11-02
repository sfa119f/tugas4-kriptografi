from function import blockMessageToText, isPrime, makeBlockMessage
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
    lenVal, message = makeBlockMessage(p-1, plainText)
    print(message)
    # k = random.randint(0,p-1)
    k = 1520
    cipherA = g ** k % p
    cipherB = []
    for i in range (len(message)):
        b = y ** k * (message[i]) % p
        cipherB.append(b)
    # print(blockMessageToText(lenVal, cipherB))
    return cipherA, cipherB, lenVal

def decrypt(cipherA, cipherB, x, p, lenVal):
    invAX = (cipherA ** (p-1-x)) % p
    msg = []
    for i in range (len(cipherB)):
        w = (cipherB[i] * invAX) % p
        msg.append(w)
    print(msg)
    return blockMessageToText(lenVal, msg)
    

print(encrypt("ENCRYPT",1185,2,2357))
print(decrypt(1430,[1265, 1165, 1811, 73, 519, 619, 1884],1751,2357,2))
# print(makePlain("encryption"))