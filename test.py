
# 将输入每三个字节断开，拿出三个字节，没六个bit段开成4段
# 2**6 =4 因此有了base64编码表
# 每一段当成一个8bit看他的值，这个值就是base64编码表的索引值，找到对应字符
# 再去3个字节，同样处理，看到最后

# 例：
# abc对应ASCII码：0x61 0x62 0x63
# 01100001 01100010 01100011
# 011000 010110 001001 100011
#   24      22    9     35


alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

teststr = 'abc'
# teststr = 'ManMa'

def base64(src):
    ret = bytearray()
    length = len(src)
    r = 0
    for offset in range(0,length,3):
        if offset + 3 <= length:
            triple = src[offset:offset + 3] #切片
        else:
            triple = src[offset:]
            r = 3 - len(triple)
            triple = triple + '\x00'*r #补几个0
        # print(triple,r)

        # 将3个字节看成一个整体转换成字节bytes，大端模式
        # abc => 0x616263
        b = int.from_bytes(triple.encode(),'big') #小端模式为‘little’ encode生成二进制
        print(hex(b)) #十六进制

        # 01100001 01100010 01100011 ==> abc
        # 011000 010110 001001 100011 六位断开
        for i in range(18,-1,-6):
            if i == 18:
                index = b >> i #右移
            else:
                index = b >> i & 0x3F #0b0011 1111
            ret.append(alphabet[index]) #得到base64编码列表

        for i in range(1,r+1): #1到r，补几个0替换成几个=
            ret[-i] = 0x3D #等号的ASCII码
    return ret

print(base64(teststr))

    
