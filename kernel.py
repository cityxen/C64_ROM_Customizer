print ()
print ("DEADLINE'S COMMODORE 64 ROM CUSTOMIZER")
print ()

c64colors = {
0:"Black",
1:"White",
2:"Red",
3:"Cyan",
4:"Violet",
5:"Green",
6:"Blue",
7:"Yellow",
8:"Orange",
9:"Brown",
10:"Light red",
11:"Dark grey",
12:"Grey",
13:"Light green",
14:"Light blue",
15:"Light grey",
}

from pathlib import Path
data = Path('kernel.rom').read_bytes()
if (data != None):
    print ("KERNEL FOUND:")
    print ("======================================")
    l1=[]
    l2=[]
    l3=[]
    i=0
    while i < 35:
        l1.append(chr(data[i+1141])) # use ord to reverse
        i += 1
    i=0
    while i < 17:
        l2.append(chr(data[i+1178])) # use ord to reverse
        i += 1
    i=0
    while i < 16:
        l3.append(chr(data[i+1121])) # use ord to reverse
        i += 1
    border = data[3289]
    bkg    = data[3290]
    txt    = data[1333]
    line1=''.join(l1)
    line2=''.join(l2)
    line3=''.join(l3)   
    print ("line1 [",line1,"]")
    print ("line2 [",line2,"]","[",line3,"]")
    print ("border:",border," (",c64colors[border],")")
    print ("bkg   :",bkg," (",c64colors[bkg],")")
    print ("txt   :",txt," (",c64colors[txt],")")
else:
    print ("NO KERNEL ROM FOUND")

from pathlib import Path
data = Path('basic.rom').read_bytes()
if(data != None):
    print ()
    print ("BASIC FOUND:")
    print ("======================================")
    r1=[]
    i=0
    while i < 6:
        r1.append(chr(data[i+888])) # use ord to reverse
        i += 1
    ready=''.join(r1)
    print ("ready :",ready)

else:
    print ("NO BASIC ROM FOUND")

print()
print()

