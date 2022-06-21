s="  tamil  "
print(len(s))
print(s.strip())
print(len(s.strip())) #strip function used to removi white space on both right side and left of the string

print(s.lstrip())
print(len(s.lstrip())) #lstrip function used to removi white space on left side of the string
print(s.rstrip())
print(len(s.rstrip())) #rstrip function used to removi white space on right side of the string


""" partision function to split the date and time"""

k='20/03/2020'
print(k.partition("/"))
print(k.split("/"))