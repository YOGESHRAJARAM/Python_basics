# dictionary function
# by using this dictionary function we can store bothe key and element in the program

user={
    "name":"Mani",
    "age" : 12,
    "father":"raja",

}

print(user)
print("---------------------------------------------------------------------")
print('\n')
# to print specific element using keyword

print(user["name"])
print(user["age"])
print("---------------------------------------------------------------------")
print('\n')
# we can use get function to find the user name
print(user.get('age'))
# to print the keys in the dictionary use key function
print(user.keys())
# to print only the values of the dictionary
print(user.values())
# to print separate keys and values use iterm function
print(user.items())
print("---------------------------------------------------------------------")
print('\n')
# to print by using loop

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x,y in user.items():
    print(x,y)

for x in user:
    print(x,":",user[x])    

# to update teh dictionary you should use the update function

user.update({"gender":"male"})
print(user.items())
print("---------------------------------------------------------------------")
print('\n')
# we can change the valuse 

user["age"]=19
print(user)

print("------- we can use pop function to remove the element----------------")
print('\n')
user.pop("age")
print(user)

print('\n')
print("-----------------------")
#nested dictionary 
users={
      "user1":{"name":"tom",},
      "user2":{"solo":"no1"}

      }
print(users)