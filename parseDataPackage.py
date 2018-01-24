import struct

rfilePath = '.\\2.txt'
wfilePath = '.\\output.txt'
wFileObj = open(wfilePath, 'a')

with open(rfilePath, 'rb') as f:
    while True:
        token = f.read(32)
        if not token:
            break
        if token.__sizeof__() != 65:
            break
        tokens = struct.unpack('!12h1q', token)
        line = ''
        for x in tokens:
            line += str(x)
            line += ','
        wFileObj.write(line[:-1])
        wFileObj.write('\n')
    f.close()
wFileObj.close()