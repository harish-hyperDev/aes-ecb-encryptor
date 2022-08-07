from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 16 # Bytes

input_msg = bytes(input("Enter Text: "), encoding='utf-8')
key = bytes(input("Enter Key: "),encoding='utf-8')

cipher = AES.new(key, AES.MODE_ECB)

msg = cipher.encrypt(pad(input_msg, BLOCK_SIZE))
bmsg = base64.b64encode(msg)

print("Encrypted String: "+bmsg.decode())

#decipher = AES.new(key, AES.MODE_ECB)
#msg_dec = decipher.decrypt(msg)
#print(unpad(msg_dec, BLOCK_SIZE).decode())