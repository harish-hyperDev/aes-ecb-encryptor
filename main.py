from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64
import pyperclip as clip
import getpass # for hiding text on type
import sys # for getting sys.argv

BLOCK_SIZE = 16 # 16 Bytes indicating AES-128 ECB

input_msg = None
key = None

try:
    if sys.argv[1] == "--hidden":
        input_msg = bytes(getpass.getpass("Enter Text: "), encoding='utf-8')
        key = bytes(getpass.getpass("Enter Key: "), encoding='utf-8')

except:
    if input_msg is None and key is None:   # if argv[1] is not hidden(i.e, None)
        input_msg = bytes(input("Enter Text: "), encoding='utf-8')
        key = bytes(input("Enter Key: "),encoding='utf-8')

cipher = AES.new(key, AES.MODE_ECB)

msg = cipher.encrypt(pad(input_msg, BLOCK_SIZE))
bmsg = base64.b64encode(msg)

# print("Encrypted String: "+bmsg.decode())
clip.copy(bmsg.decode())
print("--------------------------------------------------")
print("|                                                |")
print("|  Encrypted String is copied to your clipboard  |")
print("|                                                |")
print("--------------------------------------------------")
#decipher = AES.new(key, AES.MODE_ECB)
#msg_dec = decipher.decrypt(msg)
#print(unpad(msg_dec, BLOCK_SIZE).decode())
