from function import blockCipherToStr, blockMessageToText, isPrime, makeBlockMessage, strToBlockCipher
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
    message = makePlain(plainText)
    lenVal, blockMsg = makeBlockMessage(p-1, message)
    k = random.randint(0,p-1)
    cipherA = g ** k % p
    cipherB = []
    for i in range (len(blockMsg)):
        b = y ** k * (blockMsg[i]) % p
        cipherB.append(b)
    listB = blockCipherToStr(lenVal, cipherB)
    return cipherA, listB, lenVal

def decrypt(cipherA, cipherB, x, p, lenVal):
    blockB = strToBlockCipher(lenVal, cipherB)
    invAX = (cipherA ** (p-1-x)) % p
    msg = []
    for i in range (len(blockB)):
        w = (blockB[i] * invAX) % p
        msg.append(w)
    return blockMessageToText(lenVal, msg)
    
y,g,p = makePublicKey(2357,2,1751)
x,p = makePrivateKey(1751,2357)
cipherA,cipherB,lenVal = encrypt("hello alice",y,g,p)
print("(" + str(cipherA) + "," + str(cipherB) + ")")
print(decrypt(cipherA,cipherB,x,p,lenVal))