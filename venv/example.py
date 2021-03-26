g=2424578954555555555555555555555555550000999555555555555555555555555555555555551
print(g)
import numpy as np
import matplotlib.pyplot as plt

d=152
e=25
h="safasffasf6"
print(d,e,d/e)
print(d%25)

print (h.isalpha())

a='A'

def f(a):
    if a>0:
        print("is positive")
    else:
        print("is not positive")

v=np.random.randn(1000)
x=np.linspace(-10,10,1000)
#plt.plot(x,np.cos(x))
#plt.plot(x,np.sin(x))
#plt.scatter(x,v)
#plt.show()
c=np.random.uniform(size=1000)
#plt.plot(c)

plt.hist(c, edgecolor='black')
#plt.hist(v, edgecolor='black')
plt.show()
#for i in range(10):
#    f(e)


