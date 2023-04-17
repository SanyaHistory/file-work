# задание 1
a = [1, 1, 2, 3, 5, 8, 13, 21]
for i in a:
    if i<5:
        print(i)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
f=[]
g=set()
for h in a:
    for k in b:
        if h==k:
          g.add(h)
          f=list(g)
print(f)
# задание 2
m={'ggg': 4, 'hhh': 8,'sss': 7,'aaaa': 3,'ttt': 2}
g=(sorted(m.items(),key=lambda x: -x[1]))
g1=(sorted(m.items()))
print(g)
print(g1)
# задание 3
fh={'g': 31, 'h': 28,'s': 17,'a': 43,'t': 22}
# задание 4
fg=list(set(fh.items()))
sa=list(set(m.items()))
d=fg+sa
h=set(d)
k=dict(h)
print(k)
# задание 5
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
d=set(my_dict.items())
f=sorted(d,key=lambda x: -x[1])
c1=list(dict(f).keys())
print(c1[0],c1[1],c1[2])
# задание 6
print(int('ABC',16))
# задание 7
c2='казак'
x1=c2
x2=c2[::-1]
if x1==x2:
    print('это слово - полиндром')
else:
    print('это слово - не полиндром')
# задание 8
I=45


#X1=input('введите символ')
#f1=input('введите строку')
#sk=0
#for ig in f1:
    #if ig==X1:
        #sk=sk+1
#print(sk)

def GOTTT(*args):
   g1=args
   for i in g1:
       if i%15==0:
           print(i)

GOTTT(1,2,30,45,60,70,12,23)

def SOBR():
    DF=[]
    print('Введите 10 слов')
    i=0
    while True:
        i=i+1
        FF=input('-')
        DF.append(FF)
        if i==10:
            print('Вы ввели 10 слов')
            break
        if FF=='end':
            raise TypeError('Тут мы и завершим  работу')





def Fagot(N):
    from math import log,modf
    gas=modf(log(N,3))
    if gas[0]==0.0:
        print('Yes')
    else:
        print('No')

Fagot(9)

from threading import Timer
import time
def gosdr():
    print('Почему-то часто никак как-то получилось')

ghj=int(input('-'))
ffi=Timer(6.0,gosdr)
ffi.start()
for i in range(ghj):
    print(ghj)
    ghj-=1
    time.sleep(0.6)



