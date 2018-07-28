import re
import binascii

array=list()

def multiline_input(sentinel=''):
    while True:
        inp = input("enter an array \n")
        inp = inp.replace(" ", "")
        inp = inp.replace(",","")
        inp = inp.replace("byte.MaxValue","255")
        if inp != sentinel:
            yield inp.split()
        else:
            break

lis = list(multiline_input())
first=(str(lis[0]))
#print(lis)
n=0
for i in lis:
    s=str(lis[n])
    #print(s)
    result = re.search('\'(.*)\'', s)
    #print (result.group(1))
    array.append(int(result.group(1)))
    n+=1

#print(array)
out=binascii.hexlify(bytearray(array))
out=str(out)
out=out.replace("b'","")
out=out.replace("'","")
out=out.upper()
print(out)
