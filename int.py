# 2진,
a=23
print(type(a))
print(isinstance(a, int))

b = 0b1101
o = 0o23
h = 0x23
print(b, o, h)

#3.x에서는 int와 long 이 합쳐짐.
e = 2**1024
print(e, type(e))
print((e.bit_length()))

# 변환 함수
print(oct(38))
print(hex(38))
print(bin(38))

