"""s="tamil nadu"
print(s[0])
print(s[-1])
print(s[:4])
print(s[4:])
print(s[3:7])
print(s[::-1])
"""
w=input("inter the number :")
print(w)
if w == w[::-1]:
    print("palindrom")
else:
    print("no not a palindrom")