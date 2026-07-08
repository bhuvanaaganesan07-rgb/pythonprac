Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=1
type(a)
<class 'int'>
float(a)
1.0
b=1
a>b
False
v=(1,2,3)
type(v)
<class 'tuple'>
d={1:'one',2:'two'}
d.keys()
dict_keys([1, 2])
d.get(2)
'two'
d[1]
'one'
d[1]='three'
d
{1: 'three', 2: 'two'}
a=3
b=7
if a>b:
    print("a is greater")

    



if a>b:
    print("a is greater")
else:
    print(" b")

    
 b
if a>b:
    print("a is greater")
elif a>5:
    print(" great")
    else:
        
SyntaxError: invalid syntax
a=2
b=5
a+b
7
a+=b
a
7
a+=2
a
9
a=-a
a
-9
a>b
False
a>b and b<a
False
