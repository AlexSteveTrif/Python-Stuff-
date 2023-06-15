import numpy as np



#%%
a = np.array([1,2,3])
print(a)
#%%
b = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(b)
#%%
b[1,5]
#%%
b[0,1:6:2]
#%%
b[0,0:6:2]
#%%
b[0, 1:-1:2]
#%%
b[0,1:7]
#%%
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
#%%
np.random.randint(-1,5,(4,4))
#%%
np.random.randint??
#%%
arrr = np.array([[1,2,3]])
r11 = np.repeat(arrr,3,axis=1)
print(r11)
#%%
arrr = np.array([[1,2,3],[4,5,6]])
r11 = np.repeat(arrr,6,axis=2)
print(r11)
#%%
np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
#%%
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
r11 = np.repeat(c,3,axis=2)
print(r11)
#%%
d = np.full((5,5),1)


d[1:4,1:4] = np.full((3,3),0)

d[2,2] = 9

print(d)
#%%
g = np.ones((5,5))


g[1:4,1:4] = np.zeros((3,3))

g[2,2] = 9

print(g)

type(g)

#%%
a = np.array((6,5), 1:2)
print(a)

#%%
a = np.arange(1,31,1).reshape(6,5)

print(a)

a[1:2]

#%%

#%%

#%%

#%%

#%%

#%%
