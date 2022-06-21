#elif
"""write a program to find the fine amount 
wether late date is 0 no fine and for 1-5 days day will multiple by 0.5 
,for 5-10 day will multiple by 1 ,for 10-30 * 5 
"""

# for make this program little tuf i am goin to calculate days between two date
d=int(input("enter the days"))

if d == 0:
     print("good there is no fine")
elif(d>=1 and d<=5):
     print("your fine amount is",d*0.5)
     print("keep on time")
elif(d>5 and d<=10):
     print("your fine amount is",d*1)
     print("keep on time")
elif(d>10 and d<=30):
     print("your fine amount is",d*5)
     print("keep on time")
else:
     print(" you are too munch exeed ")