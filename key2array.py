import binascii

n=0
key = input("please enter your key ")
name = input("please enter key name ")

elements = binascii.unhexlify(key)
# Create immutable bytes object.
data = bytes(elements)

# Loop over bytes.
for d in data:
    inp=str(d)
    medium=inp.replace("255","byte.MaxValue")
    out=name + "[" + str(n) + "] = " + medium + ";"
    print(out)
    n+=1
