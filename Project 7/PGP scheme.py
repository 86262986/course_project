from gmssl import sm2
from Crypto.Cipher import AES
import random

#sm2加解密
sk = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
pk = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
sm2_crypt = sm2.CryptSM2(public_key=pk, private_key=sk)

def SM2_encrypt(P):
    C = sm2_crypt.encrypt(P)
    return C 

def SM2_decrypt(C):
    P = sm2_crypt.decrypt(C).decode(encoding="utf-8")
    return P 

#AES填充，加解密
def add_to_16(M):
    '''明文不足16位倍数，用'\0'填充'''
    if len(M.encode(encoding='utf-8')) % 16:
        add = 16 - (len(M.encode(encoding='utf-8')) % 16)
    else:
        add = 0
    M = M + ('\0' * add)
    return M.encode(encoding='utf-8')

def AES_encrypt(M,k): 
    mode = AES.MODE_CBC
    iv = b'qqqqqqqqqqqqqqqq'
    M = add_to_16(M)
    cryptos = AES.new(k, mode, iv)
    C = cryptos.encrypt(M)
    return C

def AES_decrypt(C,k): 
    iv = b'qqqqqqqqqqqqqqqq'
    mode = AES.MODE_CBC
    cryptos = AES.new(k, mode, iv)
    P = cryptos.decrypt(C)
    return bytes.decode(P).rstrip('\0')

#PGP加解密
def PGP_encrypt(M,ks): #k,会话密钥
    C1 = AES_encrypt(M,ks) #使用会话密钥ks，加密消息M
    C2 = SM2_encrypt(ks) #使用公钥pk，加密会话密钥ks 
    return C1, C2

def PGP_decrypt(C1, C2):
    ks = SM2_decrypt(C2) #使用私钥sk解密,得到会话密钥ks
    M = AES_decrypt(C1,ks.encode(encoding='utf-8')) #使用ks解密，得到消息M
    return ks,M

if __name__ == "__main__":
    M = 'plaintext'
    print("消息M：", M)
    ks = hex(random.randint(2 ** 63, 2 ** 64))[2:].encode(encoding='utf-8')
    print("随机生成会话密钥ks：", ks)
    C1, C2 = PGP_encrypt(M, ks)
    print("使用会话密钥ks，加密消息M，得到C1：", C1)
    print("使用公钥pk，加密会话密钥ks，得到C2：", C2)
    ks2, M2 = PGP_decrypt(C1, C2)
    print("使用私钥sk解密C2,得到会话密钥ks：", ks2)
    print("使用会话密钥ks解密C1，得到消息M：", M2)
