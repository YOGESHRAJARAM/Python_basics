# bitwise operator
"""
*to learn bitwise operator you have to under stand 
 how to convert decimel number into binary degits..

*for this purpose we have to know LCM concept in mathematics
 for example if we take 10 as a desimel numner to find the 
 binary..... eg:
        
        base value
        (menimum value multiple
         by this number).................   2|  10
                                              _______
                                            2|  5    -------0
                                              _______
                                            2|  2    -------1
                                              _______

                                                 1   -------0

"""

# " && "simple is user fro bitwise and operator when ther is 1  is 1 other wise 0
#                                                            1
c=10
g=11
print(c&g)
# the out put will be 10 because 1010
#                             (+)1011
#                              _______
#                                1010 ------- binary value of 10 in 1010

"another example"
a=45
b=25
print(a&b)

# " | " symbol is used for bitwise " or "operator
# in this operator if any 1 is present then the result is 1
# eg : 1 0 1 0
#      1 1 0 0
#     _________
#      1 1 1 0

print(a|b)

# ^ symbol is used for bitwise " xor "operator 
# in this operator if bothe are same then the result will be 0
# eg : 1   0   1
#      1   0   0
#      ___________
#      0   0   1

print(a^b)

# ~  bitwise not operator
# in this not operator take the variable as 10 now 10+1 then it change into 11 and next put(-)symbol 
# --in the frent of variable
print(~a)
print(~b)
print(~c)
print(~g)

# << left shift operator 
"""
 For example take 25 decimel number and convert it into binary = 11001
 now 11001 is an 5 bit operator let conver it into 8 bit operator.. for this
 purpo swe should add "000" in the frent of binary degits "00011001" ..now 
 using left shift >>2 operator we have to shift the binary degit two steps 
left side 01100100-----> 101100 now the decimal value of 1100100 is 100

"""
print(b<<2)
"""
the same methode is followed by right side shift >>2 
the value move towords right side 
"""
# 00011001 is conver 
print(b>>2)
print(a>>2)