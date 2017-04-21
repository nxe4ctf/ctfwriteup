## 
# Script for picoCTF 2017: computeAES
# Created by nxe
##

from Crypto.Cipher import AES
import base64

ciphertext = "I300ryGVTXJVT803Sdt/KcOGlyPStZkeIHKapRjzwWf9+p7fIWkBnCWu/IWls+5S"
key = "iyq1bFDkirtGqiFz7OVi4A=="

encrypted = base64.b64decode(ciphertext)
key = base64.b64decode(key)

obj = AES.new(key, AES.MODE_ECB)

print(obj.decrypt(encrypted))
