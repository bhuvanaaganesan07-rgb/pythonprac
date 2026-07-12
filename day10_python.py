Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
tuple=(2,3,4,6,7,9)
tuple
(2, 3, 4, 6, 7, 9)
tuple[0]
2
tuple[3]=7
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tuple[3]=7
TypeError: 'tuple' object does not support item assignment

s={2,3,4,5,6,9}
s
{2, 3, 4, 5, 6, 9}
s={2,3,4,5,5}
s
{2, 3, 4, 5}
s={24,84,59,73,50,84}
s
{50, 84, 24, 73, 59}
s[2]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
set.update(20)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    set.update(20)
TypeError: descriptor 'update' for 'set' objects doesn't apply to a 'int' object
s.update(1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.update(1)
TypeError: 'int' object is not iterable
s.pop()
50
s.pop()
84
s.remove(59)
s
{24, 73}
