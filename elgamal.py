from function import *

def isElGamalValidateG(g,p):
# Melakukan validasi nilai g dengan syarat algoritma
    if(g<p):
        return True
    else:
        return False

def isElGamalValidateX(x,p):
# Melakukan validasi nilai x dengan syarat algoritma
    if(x>=1 and x<=p-2):
        return True
    else:
        return False

def isElGamalValidateK(k,p):
# Melakukan validasi nilai k sesuai dengan syarat algoritma
    if (k>=0 and k<=p-1):
        return True
    else:
        return False

def makePublicKeyElGamal(g,p,x):
# Membuat kunci publik algoritma elgamal
    y = g ** x % p
    return y,g,p

def makePrivateKeyElGamal(x,p):
# Membuat kunci private algoritma elgamal
    return x,p

def encryptElGamal(plainText, y, p, g, k):
# Melakukan enkripsi pesan menggunakan algoritma elgamal
    message = makePlain(plainText)
    lenVal = lenValCipher(p-1)
    blockMsg = makeBlockMessage(lenVal,message)
    cipherA = g ** k % p
    cipherB = []
    for i in range (len(blockMsg)):
        b = y ** k * (blockMsg[i]) % p
        cipherB.append(b)
    listB = blockCipherToStr(2*lenVal, cipherB)
    return cipherA, listB

def decryptElgamal(p, g, x, k, cipher):
# Melakukan dekripsi cipher menggunakan algoritma elgamal
    lenVal = lenValCipher(p-1)
    blockB = strToBlockCipher(2*lenVal, cipher)
    cipherA = g ** k % p
    invAX = (cipherA ** (p-1-x)) % p
    msg = []
    for i in range (len(blockB)):
        w = (blockB[i] * invAX) % p
        msg.append(w)
    return blockMessageToText(lenVal, msg)