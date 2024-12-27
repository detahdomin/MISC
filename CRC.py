from zlib import crc32
import random

char = "0123456789"

def crc32_f(data):
    return hex(crc32(data.encode()) & 0xffffffff)[2:10]

length = int(input("请输入长度:"))
crc32_input = input("请输入 CRC32值:").lower()

while True:
    text = ''.join((random.choice(char)) for _ in range(length))
    if crc32_f(text) == crc32_input:
        input('找到匹配值:'+text)
        exit()
