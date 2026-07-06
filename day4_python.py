Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num = 5
type(num)
<class 'int'>
num = 7.5
type(num)
<class 'float'>
num = 5+6j
type(num)
<class 'complex'>
n=9.8
m=int(n)
type(m)
<class 'int'>
b
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b
NameError: name 'b' is not defined

m
9
a=3
b=float(a)
type(b)
<class 'float'>
b
3.0
a=1
b=2
c=complex(a,b)
type(c)
<class 'complex'>
c
(1+2j)
a<b
True
a=[1,2,3,4,4,5,6,6]
type(a)
<class 'list'>
b={1,2,3,3,4,4}
type(b)
<class 'set'>
c=(1,2)
type(c)
<class 'tuple'>
range(10)
range(0, 10)
list(range)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list(range)
TypeError: 'type' object is not iterable
list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(2,10,2))
[2, 4, 6, 8]
d={"bhuvana":"iphone","kishan":"samsung","bhavana":"one plus"}
d
{'bhuvana': 'iphone', 'kishan': 'samsung', 'bhavana': 'one plus'}
d.value()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
d.values()
dict_values(['iphone', 'samsung', 'one plus'])
d.key()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
d.keys()
dict_keys(['bhuvana', 'kishan', 'bhavana'])
d['kishan']
'samsung'
d.get("kishan")
'samsung'

