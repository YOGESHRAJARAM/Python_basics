""" continue statement ,to print add number """
from ast import Continue


i=1
while i<=20 :
    if i%2==0: 
       i=i+1 
    Continue; 
    print(i)
    i+=1
print("------------------------------")

i=2
while i<=20 :
    if i%2!=0: 
       i=i+1 
    Continue; 
    print(i)
    i+=1
