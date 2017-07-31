from Crypto.Cipher import AES
import base64
import os
import hashlib

class my_encryption():
    def __init__(self):
        self.key="hell"*8
        self.BLOCK_SIZE = 32
        self.PADDING = '{'
        self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING
        
        self.EncodeAES = lambda c, s: base64.b64encode(c.encrypt(self.pad(s)))
        self.DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(self.PADDING)
        self.cipher = AES.new(self.key)
        
    def encrypt(self,text):
        
           
        
        encoded = self.EncodeAES(self.cipher, text)
        
        return encoded
        
    def decrypt(self,text):
        
        decoded = self.DecodeAES(self.cipher, text)
        
        return decoded
    
    def Encrypt_Password(self,password):
        
        # This is one way encryption
        encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
        return encrypted_pass
        
