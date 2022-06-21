# in this session we are going to see about the cosept of Tuple funtion
# tuple functions are inmutable
"""
we use () round bracket to denote tuple

"""
# we can use any type of variable in side the tuples

a=(1,2,2.5,'tamil')
print(a)
print(type(a))

# we ca find the values in the index 

print(a[0])
print(a[3])
print(a[0:2])
print(a[0:1])

# we can also find the negative index of the tuple

print(a[-1])
print(a[-2])
print(a[0:-1])
print(a[0:-3])

# tuple is inmutuble but we can change it into list and manupulate it

b=list(a)
print(type(b))

# we can add valuse by using append function

print(b)
b.append("raja")
print(b)

# and also we conver this into tuple 

a=tuple(b)

# we can use for statement  in tuple

for i in a :
    print(i)

# if statement in tuple

if "raja" in a:
    print("raja in a")
else:
    print("raja was not in a")

# print the length of tuple

print(len(a))

#deleting the tuple by using 

del a

# adding two tuple into one tuple


a=(1,2,3,4,4,5)
b=(6,7,8,9,10)
c=a+b
print(c)
print(type(c))

# we can count the specefic number present how many time in the typle by using tuple

print(c.count(4))

# this is called nested tuples

c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])

# we can print the typles multiple times we want

x=("yogi",)*10
print(x)

# to find the minimum and the maximum value of tuple
print(min(a))
print(max(a))
