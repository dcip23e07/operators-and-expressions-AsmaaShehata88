"""
convert 4999 to base 2 using python
convert 2111 to base 2 using python
what will be the value of 4999 2111
what will be the value of 4999 | 2111
"""
first_number = 4999
first_number_bin = bin(first_number)
print(first_number_bin) #Result: 0b1001110000111

second_number = 2111
second_number_bin = bin(second_number)
print(second_number_bin) #Result: 0b100000111111


first_value = 4999 & 2111
print(first_value) #Result: 7

second_value = 4999 | 2111 
print(second_value) #Result: 7103