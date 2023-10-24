"""
var_a = 1500 + 3000 var_b = 1500 + 3000.00 var_c = 1000/5 var_d = 1200 + "200" var_e = "3004" + "996"

print the result of var_a and var_b to your terminal
Is there any difference between var_a and var_b, can you explain the differece (use comments)
what type of object is var_c
what is the value of var_d? what happened when you tried to run that expression?
what is the value of var_e? and what object is it?
"""

var_a = 1500 + 3000 #int
var_b = 1500 + 3000.00 #float
var_c = 1000/5 #float
#var_d = 1200 + "200" ---> it gave an error because an integer can not be add to a string
var_d = 1200 + 200 #int
var_e = "3004" + "996" #str

print(var_a)
print(var_b)
print(type(var_c))
print(var_e)
print(type(var_e))