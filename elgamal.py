from function import *
import random

def makePublicKey(p,g,x):
# Membuat kunci publik algoritma elgamal
    if(isPrime(p) and g<p and x>=1 and x<=p-2):
        y = g ** x % p
        return y,g,p

def makePrivateKey(x,p):
# Membuat kunci private algoritma elgamal
    if(isPrime(p) and x>=1 and x<=p-2):
        return x,p

def encrypt(plainText, y, g, p):
# Melakukan enkripsi pesan menggunakan algoritma elgamal
    message = makePlain(plainText)
    lenVal = lenValCipher(p-1)
    blockMsg = makeBlockMessage(lenVal,message)
    k = random.randint(0,p-1)
    cipherA = g ** k % p
    cipherB = []
    for i in range (len(blockMsg)):
        b = y ** k * (blockMsg[i]) % p
        cipherB.append(b)
    listB = blockCipherToStr(2*lenVal, cipherB)
    return cipherA, listB, lenVal

def decrypt(cipherA, cipherB, x, p, lenVal):
# Melakukan dekripsi cipher menggunakan algoritma elgamal
    blockB = strToBlockCipher(2*lenVal, cipherB)
    invAX = (cipherA ** (p-1-x)) % p
    msg = []
    for i in range (len(blockB)):
        w = (blockB[i] * invAX) % p
        msg.append(w)
    return blockMessageToText(lenVal, msg)