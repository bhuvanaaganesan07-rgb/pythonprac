Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
nums=[23,45,67,74,90]
nums
[23, 45, 67, 74, 90]
nums[0]
23
nums[-1]
90
nums[1]=33
nums
[23, 33, 67, 74, 90]
names=['kishan','kiran','bhavana','bhuvana']
names
['kishan', 'kiran', 'bhavana', 'bhuvana']
list=[nums,names]
list
[[23, 33, 67, 74, 90], ['kishan', 'kiran', 'bhavana', 'bhuvana']]
nums
[23, 33, 67, 74, 90]
nums.append(99)
nums
[23, 33, 67, 74, 90, 99]
nums.insert(2,45)
nums
[23, 33, 45, 67, 74, 90, 99]
nums.remove(99)
nums
[23, 33, 45, 67, 74, 90]
nums.pop()
90
nums.pop(3)
67
nums
[23, 33, 45, 74]
del nums

names
['kishan', 'kiran', 'bhavana', 'bhuvana']
del names[2:]
names
['kishan', 'kiran']
names.extend(['bhuvana','bhavana'])
names
['kishan', 'kiran', 'bhuvana', 'bhavana']
nums=[2,3,4,5,6,7,8,9]
nums
[2, 3, 4, 5, 6, 7, 8, 9]
min(nums)
2
max(nums)
9
sum(nums)
44
nums
[2, 3, 4, 5, 6, 7, 8, 9]
mean(nums)

nums.sort()
nums
[2, 3, 4, 5, 6, 7, 8, 9]
