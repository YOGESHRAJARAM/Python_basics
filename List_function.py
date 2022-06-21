# sample program to know the list function
# list functio is simeler to array but the mail defferense is list is changeable and array must be in same type..
from pickle import TRUE


a={1,2,3,4,5} #-------is an array
print(a)

print("------------------------------------")
B = [0,0.12,"tamil"]
print(B[0],type(B[0]))
print(B[1],type(B[1]))
print(B[2],type(B[2]))

print("--------------------------------------")

#to print last number

print(B[-1])
print(B[0:-1])
print(B[:2])
print(B[1:])

print("--------------------------------------") 
#clear function in list

C = [76,54,3,23]
print("before clearing the list",C)
C.clear()
print("using .clear() function to clear the list")
print("after clearing the list",C)

print("--------------------------------------") 
#copy function in list

print(" using .copy function to copy one list from another list")
D=B.copy()
print(D)
print(D.count(0))
print(D.index(0.12))
print(len(a))
print(max(a))
print(min(a))
print("--------------------------------------") 
k=[1,3,4,5,6,67]
print(k)
k.pop(0)
print(k)
k.remove(5)
print(k)
print("--------------------------------------") 

#append function 
name=['tamil','ganesg']
print(name)
name.append('yogesh')
name.append('pradeep')
print(name)

print("--------------------------------------") 
names=["gokul"]
name.extend(names)
print(name)

print("--------------------------------------") 
name.insert(2,"tamizhal")
print(name)
print("--------------------------------------") 
#list()
print(list(range(2,20,1)))
#sort()
k=[54,4,23,1]
k.sort()
print(k)
k.sort(reverse=True)
print(k)
