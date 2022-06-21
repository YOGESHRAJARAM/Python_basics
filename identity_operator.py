#identity_operator
"""
In this operator we can find wether the object is true or not 
 we use :" is ", "not is " Operator
        
"""
a=[1,2,3]
c=[1,2,3]
k=[9,8]
b = a
print(a is b)
print(a is c)# the out will false because here the id of the two object will different
if a is b :
    print( " both are same so print as True")
print(id(a))
print(id(b))
print(id(c))

# in this out put we can find every object fave separate id 
# but to cheack the valuse use' == 'operator

print(a==c)

# is not " this will totaly agains the is operator"
print(a is not b)
print(a is not  c)

# to compare the values use '!= 'operator
print( a != b)
print( a != k)