from base64 import encode
from string import ascii_letters, digits

base62 = digits + ascii_letters
base62Size = len(base62)

def encodeBase62(number, encoded=''):
    return encodeBase62(number//base62Size, base62[number%base62Size] + encoded) if number >= base62Size else base62[number%base62Size] + encoded

def decodeBase62(text,decoded=0):
    return decodeBase62(text[1:], decoded*base62Size + base62.index(text[0])) if text else decoded


"""
def search4patterns(salt,patterns2find):
    try:

    except:
"""