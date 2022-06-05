from base64 import encode
from string import ascii_letters, digits
from hashlib import sha256

base62 = digits + ascii_letters
base62Size = len(base62)

def encodeBase62(number, encoded = ''):
    return encodeBase62(number//base62Size, base62[number%base62Size] + encoded) if number >= base62Size else base62[number%base62Size] + encoded

def decodeBase62(text,decoded = 0):
    return decodeBase62(text[1:], decoded*base62Size + base62.index(text[0])) if text else decoded

def generateFixedLenghtCode(targetLenght, seed = ''):
    if targetLenght < 1:
        raise('Lenght must be a non null positive number')

    overMaximum = base62Size**targetLenght
    minimum = base62Size**(targetLenght -1)   
    baseHash = int(sha256(seed.encode()).hexdigest(),16)
    #make it better!!!!!!
    if baseHash >= overMaximum:
        baseHash = int(((baseHash**(-1))+(overMaximum**(-1)))**(-1))

    if baseHash < minimum:
        baseHash += minimum

    return encodeBase62(baseHash)