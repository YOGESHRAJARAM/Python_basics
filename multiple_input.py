""""
"In Normal input..........method 1"
name=input("enter the name:")
print("Your Enter Name id : ",name)

"""""
"""""
"Another multiple input........ method2"
name1,name2,name3=input("Enter any three name").split()
print("name1 :",name1)
print("name2 :",name2)
print("name3 :",name3)

"""""
"""""
"in above mention methow we cant able to split the name into first name and last name for this resion use .split function with , .split(',')"
name1,name2,name3=input("Enter any three name").split(',')
print("name1 :",name1)
print("name2 :",name2)
print("name3 :",name3)

"""""