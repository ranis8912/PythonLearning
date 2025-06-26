#Exception handling in Python
a=int(input('Enter a: '))
b=int(input('Enter b: '))
try:
    c=a/b
    print('c ',c)
except:
    print('b must be non zero')
print('a is ',a)
print('b is ',b)
print('Hello')
#module not found
try:
    import abdc
    abcd.test()
except:
    print('may be import error')
#Type Exception
b=20
try:
    print(str(b))
except:
    print('Type Exception string')
a='hello'
try:
    print(int(a))
except:
    print('Type Exception INT')
#File not Found
try:
    f=open('myfile.txt','r')
    content = file.read()
    print(content)
except:
    print('File not found')
#indentation exception
for i in range(10):
 print('i is ',i)
#Index out of Range
L=[10,20,30]
try:
    print(L[10])
except:
    print('Index outbound')
