"now we are going to get para as input"
"""
para=[]
print("Enter the para:" )
"""
"""in this above code the user and program not konw where to stop 
for that reasion we create one while loop"""
from collections import namedtuple


para=[] #n this para we are going to store value
print("enter the paragraph")

while True: #we use this to cheack wethe the line is true that means is there is line or blank
    line=input()
    if line: #if the line is enter it's just store the value in the para variable
      para.append(line) #.append function is used to store the value one by one
    else:
      break
output='\n'.join(para) # here i use \n to compain the output
print(output)
