# set is un order 
# un index
# set can be denoted by curly bracket
# we can only add or remove values in the set

a={"ram",1,2.5}
print(a)
print(type(a))

#using for loop in the set to access value

for i in a:
    print(i)

# adding elements in the set

a.add("sam")
print(a)

#to add more number of element in the set use update function

b={"raja","kannan","matakops"}
a.update(b)
print(a)
# to remove element
a.remove("kannan")
print(a)
# to remove element if it is present
a.discard("raja")
print(a)
# we can remove random valuse by using the pop () function
a.pop()
print(a)
# to clear every element in the set
a.clear()
print(a)

# if we use del set function it will totaly remove the set
del a

# in set the duplicate values are automaticaly removed

a={'a','s','d','d','f','f','g'}
print(a)
del a

# mostly we use mathematical calculation using the set functon 

a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.union(b)
print(c)

# to find intersection 
d =a.intersection(b)
print(d)
"-------to store the result in a-------- "
a.intersection_update(b)
print(a)

# to find the semitric defferent

k=a.symmetric_difference(b)
print(k)

"---------to store the result in a------"

a.symmetric_difference_update(b)
print(a)

# to find true or false wether same number present in the two set

l=a.isdisjoint(b)
print(l)
del l
l=a.issubset(b)
print(l)
del l
l=a.issuperset(b)
print(l)