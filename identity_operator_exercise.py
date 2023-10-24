"""
var_a = 400 var_b = '200' + '200' var_c = 400.0 var_d = 200 + 200

what is the result of : i. var_a == var_b ii. var_a is var_b (can you explain using comments the reason for the result)

what is the result of : i. var_a == var_c ii. var_a is var_c (can you explain using comments the reason for the result)

what is the result of : i. var_a == var_d ii. var_a is var_d (can you explain using comments the reason for the result)

"""

var_a = 400 #int
var_b = '200' + '200' #str
var_c = 400.0 #float
var_d = 200 + 200 #int

print(var_a == var_b) # False
#The result is false becuse the comparison here is between an integer and string in this case the value of var_b is 200200

print(var_a is var_b) #False because they are not he same object (integer and string)

print(var_a == var_c) #True, because they carry the same value
print(var_a is var_c) #False , because they are not the same type

print(var_a == var_d) #True, because the carry the same value
print(var_a is var_d) #True, They carry the same value and they are the same type as well



