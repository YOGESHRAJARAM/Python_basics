# if_else_statement
""" write an program to cheack the vote eligibility by entering name and age"""
name=input("Enter your Name :")
age=int(input("Enter Your Age :"))
if age >= 18:
    print(name.upper(),"age",age,"is eligble for vote")
else:
    print(name.capitalize(),"age",age,"not enough for vote")
