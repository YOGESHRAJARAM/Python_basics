# nested if satatment..
"""
find the grade of the studen and 
give result asverage and grade 
by getting three inputs marks """

m1=int(input("Enter mark one   : "))
m2=int(input("enter mark two   : "))
m3=int(input("enter mark three : "))
total = m1 + m2 + m3
average = total / 3.0
print(average)
if m1 >=35 and m2 >= 35 and m3 >=35 :
    print("Result : PASS")
    if average<=90 and average<=100:
         print("Grade : A ")
    elif average<=89 and average<=70:
         print("Grade : B ")
    elif average<=79 and average<=60:
         print("Grade : B ")    
    elif average<=59 and average<=40:
         print("Grade : C ")
else:
    print("Result : FAIL")
    print("No Grade")